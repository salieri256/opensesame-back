from pydantic import BaseModel, Field

class DoorBase(BaseModel):
    name: str
    icon: str

class Door(DoorBase):
    id: int
    isLocked: bool

    class Config:
        orm_mode = True