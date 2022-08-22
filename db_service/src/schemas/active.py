from pydantic import BaseModel

class Active(BaseModel):
    isActive: bool

    class Config:
        orm_mode = True