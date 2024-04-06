from fastapi import FastAPI
from dataModels import userInfo
import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    dbuser="admin",
    password="password",
    host="localhost",
    port="5432"
)

app = FastAPI()

@app.post("/signup/")
async def createUser(user: userInfo):
    return {"user": user}
