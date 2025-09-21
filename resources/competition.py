# competition.py

from db.models import Competition

class CompetitionResource:
    # list competitions
    def on_get(self, req, resp):
        session = req.context.session  # <-- use context
        competitions = session.query(Competition).all()
        resp.media = [{"id": c.id, "title": c.title} for c in competitions]

    # create competition 
    def on_post(self, req, resp):
        return
