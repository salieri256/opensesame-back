from pydantic import BaseModel

class Lock(BaseModel):
    isLocked: bool

    class Config:
        orm_mode = True