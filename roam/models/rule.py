from sqlalchemy import Column, Integer, String
from models import Base

__author__ = 'Ryun'


class Rule(Base):
    __tablename__ = 'rule'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    keyword = Column(String(100), nullable=False)