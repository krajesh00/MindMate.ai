from pydantic import BaseModel
import datetime

class userInfo(BaseModel):
    firstName: str
    lastName: str
    age: int
    email: str
    password: str
    userName: str

class loginObject(BaseModel):
    userName: str
    password: str

class chatObject(BaseModel):
    chat_id: str
    chat: str
    time: datetime.datetime 
    resoureType: str