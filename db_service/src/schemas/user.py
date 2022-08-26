from pydantic import BaseModel, Field

class UserBase(BaseModel):
    name: str
    nfcId: str | None

class User(UserBase):
    id: int
    isActive: bool

    class Config:
        orm_mode = True