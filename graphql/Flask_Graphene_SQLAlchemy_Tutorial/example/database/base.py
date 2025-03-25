from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import os

# Create database engine
db_name = 'swapi'
# db_path = os.path.join(os.path.dirname(__file__), db_name)
# db_uri = 'postgresql://{}'.format(db_path)
db_uri = f'postgresql://dgmr2:@localhost:5432/{db_name}'
engine = create_engine(db_uri)

# Declarative base model to create database tables and classes
Base = declarative_base()
Base.metadata.bind = engine

# Create database session object
db_session = scoped_session(sessionmaker(bind=engine, expire_on_commit=False))
Base.query = db_session.query_property()