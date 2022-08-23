from pydantic import BaseModel, Field

class LockLogBase(BaseModel):
    isLocked: bool
    doorId: int
    userId: int

class LockLog(LockLogBase):
    id: int
    unixTime: int

    class Config:
        orm_mode = True