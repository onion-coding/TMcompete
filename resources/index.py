import os

class IndexResource:
    def on_get(self, req, resp):
        state = secrets.token_urlsafe(16)
        req.context.session["oauth_state"] = state
        url = (
            f"https://api.trackmania.com/oauth/authorize"
            f"?response_type=code"
            f"&client_id={os.getenv("CLIENT_ID")}"
            f"&redirect_uri={os.getenv("REDIRECT_URI")}"
            f"&state={state}"
        )
        resp.content_type = "text/html"
        resp.text = f'<a href="{url}">Login with Ubisoft</a>'
