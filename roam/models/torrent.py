from sqlalchemy import Column, Integer, SmallInteger, Date, String
from models import Base

__author__ = 'Ryun'


class Torrent(Base):
    __tablename__ = 'torrents'
    id = Column(Integer, primary_key=True)
    season = Column(SmallInteger, nullable=False)
    episode = Column(SmallInteger, nullable=False)
    date = Column(Date, nullable=False)
    resolution = Column(String(10), nullable=False)
    video_codec = Column(String(10), nullable=False)
    source = Column(String(10), nullable=True)
