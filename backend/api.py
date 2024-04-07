from fastapi import FastAPI
from dataModels.apiDataModels import userInfo
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from dataModels.dbDataModels import User
from utils.rateLimiter import RateLimiterMiddleware
from utils.tokenBucket import TokenBucket

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

bucket = TokenBucket(capacity=4, refill_rate=2)

# Add the rate limiting middleware to the FastAPI app
app.add_middleware(RateLimiterMiddleware, bucket=bucket)

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
