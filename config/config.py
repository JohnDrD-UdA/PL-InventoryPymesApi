from sqlalchemy import create_engine, MetaData
URL="postgresql://postgres:root@localhost:5433/postgres"

engine= create_engine(URL)

conn=engine.connect()

meta_data=MetaData()