from sqlalchemy import Column, Integer, Text, Boolean
from src.db import Base

class Door(Base):
    __tablename__ = 'door'

    id: int | Column = Column(Integer, primary_key=True, autoincrement=True)
    isLocked: bool | Column = Column(Boolean, default=False)
    name: str | Column = Column(Text)