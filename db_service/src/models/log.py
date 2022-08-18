from sqlalchemy import Column, Integer, Boolean
from src.db import Base

class Log(Base):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer)
    active = Column(Boolean)
    unixTime = Column(Integer)
