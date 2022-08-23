from sqlalchemy import Column, Integer, Boolean, ForeignKey
from src.db import Base
from src.models.door import Door
from src.models.user import User

class LockLog(Base):
    __tablename__ = 'lock_log'

    id: int | Column = Column(Integer, primary_key=True, autoincrement=True)
    unixTime: int | Column = Column(Integer)
    isLocked: bool | Column = Column(Boolean)
    doorId: int | Column = Column(Integer, ForeignKey(f'{Door.__tablename__}.id'))
    userId: int | Column = Column(Integer, ForeignKey(f'{User.__tablename__}.id'))