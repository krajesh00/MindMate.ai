from fastapi import FastAPI
from apiDataModels import userInfo
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import Session
from dbDataModels import User

# import psycopg2

# conn = psycopg2.connect(
#     dbname="postgres",
#     dbuser="admin",
#     password="password",
#     host="localhost",
#     port="5432"
# )

engine = create_engine('postgresql://admin:example@localhost:5432/userdb')

app = FastAPI()

@app.post("/signup/")
async def createUser(user: userInfo):
    with Session(engine) as session:
        new_user = User(
                        username=user.userName, 
                        email=user.email, 
                        passphrase=user.password, 
                        age=user.age, 
                        firstname=user.firstName, 
                        lastname=user.lastName
                        )
        session.add(new_user)
        session.commit()
        return user
