from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from backend.db import Base, Money


def initialize(type, username, password, host, db_name):
    engine = create_engine("{}://{}:{}@{}/{}".format(type, username, password, host, db_name))
    session = sessionmaker(bind=engine)()
    Base.metadata.create_all(engine)
    return engine, session, Money
