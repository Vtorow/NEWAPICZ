import datetime

from pydantic import BaseModel

class CreateUser(BaseModel):
    username: str
    password: str

class User(CreateUser):
    created_at: datetime.datetime
    updated_at: datetime.datetime


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class UserInDB(User):
    hashed_password: str


class UserBook(CreateUser):
    start_time: datetime.datetime
    end_time: datetime.datetime
    comment: str