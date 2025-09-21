import falcon, os, secrets
from falcon_sqla import Manager
from db.session import engine
from dotenv import load_dotenv
from resources.callback import CallbackResource
from resources.index import IndexResource

load_dotenv()

manager = Manager(engine)
app = falcon.App(middleware=[manager.middleware])

CLIENT_ID = os.getenv("TM_CLIENT_ID")
CLIENT_SECRET = os.getenv("TM_CLIENT_SECRET")
REDIRECT_URI = "http://localhost:8000/callback"

app = falcon.App()
app.add_route("/", IndexResource())
app.add_route("/callback", CallbackResource())
