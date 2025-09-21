import falcon
from falcon_sqla import Manager
from db.session import engine
import os
from dotenv import load_dotenv

load_dotenv()

manager = Manager(engine)
app = falcon.App(middleware=[manager.middleware])

CLIENT_ID = os.getenv("TM_CLIENT_ID")
CLIENT_SECRET = os.getenv("TM_CLIENT_SECRET")
REDIRECT_URI = "http://localhost:8000/callback"

app = falcon.App()
app.add_route("/", IndexResource())
app.add_route("/callback", CallbackResource())
