from falcon import HTTP_200
from db.session import Session

class EventsResource:
    def on_get(self, req, resp):
        session = Session()
        # do queries with session
        resp.media = {"status": "ok"}
        session.close()

# endpoints
# /browse           -> browse all competitions, will be the landing page
# /contact          -> contact details: email
# /login            -> Ubisoft Connect login (redirect to Ubisoft OAuth)
# /search           -> search competitions with filters
# /saved            -> user’s saved competitions
# /admin            -> moderation dashboard (approve ads, manage users)