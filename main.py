from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from constants import DATABASE_URL
from create_table import URL_Mapper

app = FastAPI()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

@app.get("/getURL")
def getURL(url):
    hashed_url = str(hash(url))
    new_mapping = URL_Mapper(url=f"{url}", hash=f"{hashed_url}")
    session.add(new_mapping)
    session.commit()
    finalURL = "https:/sanskar/" + hashed_url
    return finalURL

