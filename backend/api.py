from fastapi import FastAPI
from dataModels.apiDataModels import userInfo
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from dataModels.dbDataModels import User
from utils.rateLimiter import RateLimiterMiddleware
from utils.tokenBucket import TokenBucket
import jwt
import dotenv
import os

dotEnvDir = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(dotEnvDir)

SECRET_KEY = os.getenv("private-key")

engine = create_engine('postgresql://admin:example@localhost:5432/userdb')

app = FastAPI()

bucket = TokenBucket(capacity=4, refill_rate=2)

# Add the rate limiting middleware to the FastAPI app
app.add_middleware(RateLimiterMiddleware, bucket=bucket)

@app.post("/signup/")
async def createUser(user: userInfo):
    encoded_jwt = ""
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
        encoded_jwt = jwt.encode({"username": new_user.id}, SECRET_KEY, algorithm=["RS256"])

    return {"token": encoded_jwt}

@app.get("/login/")
async def loginUser(username: str, password: str):
    encoded_jwt = ""
    with Session(engine) as session:
        user = session.query(User).filter(User.username == username).first()
        if user.passphrase == password:
            encoded_jwt = jwt.encode({"username": user.id}, SECRET_KEY, algorithm=["RS256"])

    return {"token": encoded_jwt}
