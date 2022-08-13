from pydantic import BaseModel, Field

class Log(BaseModel):
    id: int
    userId: int
    active: bool = Field(False, description='入室したかどうか')
    unixTime: int