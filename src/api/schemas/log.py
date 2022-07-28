from pydantic import BaseModel

class ActiveLog(BaseModel):
    id: int
    isActive: bool
    unixTime: int
    userId: int