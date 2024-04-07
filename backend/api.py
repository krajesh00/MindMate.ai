from fastapi import FastAPI, HTTPException, Request 
from dataModels.apiDataModels import userInfo, loginObject, chatObject
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from dataModels.dbDataModels import User
from utils.rateLimiter import RateLimiterMiddleware
from utils.tokenBucket import TokenBucket
import jwt
from jwt import PyJWTError
import dotenv
import os
import pymongo

dotEnvDir = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(dotEnvDir)

SECRET_KEY = os.getenv("private-key")
PUBLIC_KEY = os.getenv("public-key")

engine = create_engine('postgresql://admin:example@localhost:5432/userdb')
myclient = pymongo.MongoClient("mongodb://root:example@localhost:27017/")
mydb = myclient["chatdb"]
human_col= mydb["chatshuman"]
ai_col = mydb["chatai"]

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
        encoded_jwt = jwt.encode({"id": new_user.id}, SECRET_KEY, algorithm=["RS256"])

    return {"token": encoded_jwt}

@app.get("/login/")
async def loginUser(loginObject: loginObject):
    encoded_jwt = ""
    with Session(engine) as session:
        user = session.query(User).filter(User.username == loginObject.userName).first()
        if user.passphrase == loginObject.password:
            encoded_jwt = jwt.encode({"id": user.id}, SECRET_KEY, algorithm=["RS256"])

    return {"token": encoded_jwt}

@app.post("/chat/")
async def createChat(chatObject: chatObject, request: Request):
    try:
        auth_header = request.headers["Authorization"]
        if not auth_header or auth_header.startswith("Bearer ") == False:
            raise HTTPException(status_code=401, detail="Unauthorized")
        
        token = auth_header.split("Bearer ")[1]
        payload = jwt.decode(token, PUBLIC_KEY, algorithms=["RS256"])

        user_id = payload.get("id")
        human_col.insert_one({"user_id": user_id, "chat": chatObject.chat, "time": chatObject.time})

    except PyJWTError:
        raise HTTPException(status_code=401, detail="invalid token")
