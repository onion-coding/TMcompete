import falcon
from routes import events

app = falcon.App()

# Example route
class TestResource:
    def on_get(self, req, resp):
        events.test_query()
        resp.media = {"status": "ok"}

app.add_route("/test", TestResource())
