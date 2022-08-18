from sqlalchemy import Column, Integer, String, Boolean
from src.db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    active = Column(Boolean, default=False)
    nfcId = Column(String)
