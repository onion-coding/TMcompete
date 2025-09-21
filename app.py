import falcon
import requests
from falcon_sqla import Manager
from db.session import engine
import os
from dotenv import load_dotenv
import secrets
# from resources/callback import CallbackResource
load_dotenv()

manager = Manager(engine)
app = falcon.App(middleware=[manager.middleware])

CLIENT_ID = os.getenv("TM_CLIENT_ID")
CLIENT_SECRET = os.getenv("TM_CLIENT_SECRET")
REDIRECT_URI = "http://localhost:8000/callback"

class IndexResource:
    def on_get(self, req, resp):
        state = secrets.token_urlsafe(16)
        req.context.session["oauth_state"] = state
        url = (
            f"https://api.trackmania.com/oauth/authorize"
            f"?response_type=code"
            f"&client_id={CLIENT_ID}"
            f"&redirect_uri={REDIRECT_URI}"
            f"&state={state}"
        )
        resp.content_type = "text/html"
        resp.text = f'<a href="{url}">Login with Ubisoft</a>'

class CallbackResource:
    def on_get(self, req, resp):
        code = req.get_param("code")
        returned_state = req.get_param("state")
        expected_state = req.context.session.get("oauth_state")

        if returned_state != expected_state:
            resp.status = 400
            resp.text = "Invalid state"
            return

        token_url = "https://api.trackmania.com/api/access_token"
        data = {
            "grant_type": "authorization_code",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "code": code,
            "redirect_uri": REDIRECT_URI,
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        r = requests.post(token_url, data=data, headers=headers)
        tokens = r.json()

        # Optional test API call
        test_url = "https://api.trackmania.com/api/display-names?accountIdList=PUT_ACCOUNT_ID"
        test_headers = {"Authorization": f"Bearer {tokens['access_token']}"}
        test_resp = requests.get(test_url, headers=test_headers)

        resp.media = {
            "tokens": tokens,
            "api_test": test_resp.json()
        }

app = falcon.App()
app.add_route("/", IndexResource())
app.add_route("/callback", CallbackResource())
