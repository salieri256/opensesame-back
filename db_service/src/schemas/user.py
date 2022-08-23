from pydantic import BaseModel, Field

class UserBase(BaseModel):
    name: str
    nfcId: str | None

class User(UserBase):
    id: int
    active: bool

    class Config:
        orm_mode = True