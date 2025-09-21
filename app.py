import falcon
from falcon_sqla import Manager
from db.session import engine
from resources.callback import CallbackResource
from resources.index import IndexResource
from dotenv import load_dotenv

load_dotenv()

manager = Manager(engine)
app = falcon.App(middleware=[manager.middleware])

app = falcon.App()
app.add_route("/", IndexResource())
app.add_route("/callback", CallbackResource())
