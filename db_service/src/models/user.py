from sqlalchemy import Column, Integer, Text, Boolean
from src.db import Base

class User(Base):
    __tablename__ = 'user'

    id: int | Column = Column(Integer, primary_key=True, autoincrement=True)
    isActive: bool | Column = Column(Boolean, default=False)
    name: str | Column = Column(Text)
    nfcId: str | None | Column = Column(Text)