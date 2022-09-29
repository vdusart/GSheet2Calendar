import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

user = os.environ['POSTGRESQL_ADDON_USER']
password = os.environ['POSTGRESQL_ADDON_PASSWORD']
host = os.environ['POSTGRESQL_ADDON_HOST']
port = os.environ['POSTGRESQL_ADDON_PORT']
db = os.environ['POSTGRESQL_ADDON_DB']
URI = f"postgresql://{user}:{password}@{host}:{port}/{db}"

engine = create_engine(URI)
Session = sessionmaker(bind=engine)
Base = declarative_base()
