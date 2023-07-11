import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, CHAR

Base = declarative_base()


class Event(Base):
    __tablename__ = 'event'

    eventID = Column(Integer, primary_key=True)
    event_type = Column(Integer, nullable=False)
    event_start = Column(DateTime, nullable=False)
    event_location = Column(String(20))
    oldperson_id = Column(Integer)
    elderlyName = Column(String(20))
    __table_args__ = {
        "mysql_charset": "utf8"
    }
