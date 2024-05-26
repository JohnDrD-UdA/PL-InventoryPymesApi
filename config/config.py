from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

URL="postgresql://postgres:root@localhost:5433/postgres"

engine= create_engine(URL)

Base= declarative_base()

Session= sessionmaker(bind=engine)

session=Session()
