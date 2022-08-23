from pydantic import BaseModel, Field

class DoorBase(BaseModel):
    name: str

class Door(DoorBase):
    id: int
    lock: bool

    class Config:
        orm_mode = True