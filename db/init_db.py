from sqlalchemy import create_engine
from db.models import Base
import os
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(
    f"postgresql+psycopg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

Base.metadata.create_all(engine)
print("Tables created!")