import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

URI = os.environ.get('POSTGRESQL_ADDON_URI')

engine = create_engine(URI)
Session = sessionmaker(bind=engine)
Base = declarative_base()
