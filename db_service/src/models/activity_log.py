from sqlalchemy import Column, Integer, Boolean, ForeignKey
from src.db import Base
from src.models.user import User

class ActivityLog(Base):
    __tablename__ = 'activity_log'

    id: int | Column = Column(Integer, primary_key=True, autoincrement=True)
    unixTime: int | Column = Column(Integer)
    isActive: bool | Column = Column(Boolean)
    userId: int | Column = Column(Integer, ForeignKey(f'{User.__tablename__}.id'))