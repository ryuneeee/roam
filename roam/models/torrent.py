from sqlalchemy import Column, Integer, SmallInteger, String
from models import Base

__author__ = 'Ryun'


class Torrent(Base):
    __tablename__ = 'torrents'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    subname = Column(String, nullable=True)
    season = Column(SmallInteger, nullable=False)
    episode = Column(SmallInteger, nullable=False)
    date = Column(SmallInteger, nullable=False)
    year = Column(SmallInteger, nullable=False)
    resolution = Column(String(10), nullable=False)
    video_codec = Column(String(10), nullable=True)
    audio_codec = Column(String(10), nullable=True)
    source = Column(String(10), nullable=True)
    torrent_id = Column(Integer, nullable=False)
    link = Column(String, nullable=False)

    def __init__(self, *args, **kwargs):
        print(args, kwargs)
        if isinstance(kwargs, dict):
            for k, v in kwargs.items():
                self.__setattr__(k, v)
        else:
            raise ValueError('Invalid arguments.')
