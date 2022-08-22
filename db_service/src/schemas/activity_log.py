from pydantic import BaseModel, Field

class ActivityLogBase(BaseModel):
    isActive: bool
    userId: int

class ActivityLog(ActivityLogBase):
    id: int
    unixTime: int

    class Config:
        orm_mode = True