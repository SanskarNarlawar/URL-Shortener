from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine
from constants import DATABASE_URL

class Base(DeclarativeBase):
    pass

class URL_Mapper(Base):
    __tablename__ = "url-mapping"
    id = Column(Integer, primary_key=True)
    url = Column(String)
    hash = Column(String)

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
