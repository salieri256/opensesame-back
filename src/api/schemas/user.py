from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    uidList: list[str]

class User(UserBase):
    id: int
    isActive: bool

class UserCreate(UserBase):
    pass

class UserCreateResponse(User):
    pass