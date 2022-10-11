from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

Base = declarative_base()
_CONNECTION = "sqlite:///contacts.db"

engine = create_engine(_CONNECTION, echo=True)
metadata = Base.metadata
DBSession = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
session = DBSession()
