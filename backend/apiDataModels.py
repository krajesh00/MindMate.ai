from pydantic import BaseModel

class userInfo(BaseModel):
    firstName: str
    lastName: str
    age: int
    email: str
    password: str
    userName: str