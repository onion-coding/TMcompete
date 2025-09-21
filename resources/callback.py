import os

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
            "client_id": os.getenv("CLIENT_ID"),
            "client_secret": os.getenv("CLIENT_SECRET"),
            "code": code,
            "redirect_uri": os.getenv("REDIRECT_URI_"),
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
