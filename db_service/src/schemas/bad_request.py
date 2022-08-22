from pydantic import BaseModel
from fastapi import Request

class BadRequest(BaseModel):
    detail: str