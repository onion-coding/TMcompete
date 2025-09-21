# competition.py
import falcon
from falcon_sqla import Manager
from db.session import engine
from db.models import Competition

manager = Manager(engine)
app = falcon.App(middleware=[manager.middleware])

class TestResource:
    def on_get(self, req, resp):
        session = req.context.session  # <-- use context
        competitions = session.query(Competition).all()
        resp.media = [{"id": c.id, "title": c.title} for c in competitions]

app.add_route('/test', TestResource())
