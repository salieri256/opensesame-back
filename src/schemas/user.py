from pydantic import BaseModel, Field

class UserBase(BaseModel):
    name: str = Field('')
    nfcId: str = Field('')

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    active: bool = Field(False)

    class Config:
        orm_mode = True