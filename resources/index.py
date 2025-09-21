import os
import secrets

class IndexResource:
    def on_get(self, req, resp):
        state = secrets.token_urlsafe(16)
        req.context.session["oauth_state"] = state
        base_url = "https://api.trackmania.com/oauth/authorize"
        client_id = os.getenv("CLIENT_ID")
        redirect_uri = os.getenv("REDIRECT_URI")
        auth_url = f"{base_url}?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&state={state}"
        resp.content_type = "text/html"
        resp.text = f'<a href="{auth_url}">Login with Ubisoft</a>'
