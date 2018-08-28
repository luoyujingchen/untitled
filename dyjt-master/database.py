import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session,sessionmaker

basedir = os.path.abspath(os.path.dirname(__file__))

engine = create_engine('sqlite:///'+os.path.join(basedir,'app,db'))
db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import PicModel.Picture
    Base.metadata.create_all(bind=engine)