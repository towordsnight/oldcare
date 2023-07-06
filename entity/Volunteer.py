from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,DateTime,CHAR



Base = declarative_base()



class Volunteer(Base):
    __tablename__ = 'volunteer'

    volunteerID = Column(Integer, primary_key=True)
    volunteerName = Column(String(20), nullable=False)
    age = Column(Integer)
    gender = Column(String(20))
    id_card = Column(String(20))
    checkin_date = Column(DateTime)
    checkout_date = Column(DateTime)
    phone = Column(String(20))
    imgset_dir = Column(String(200))
    profile_photo = Column(String(200))
    description = Column(String(50))
    created = Column(DateTime)
    createby = Column(String(20))
    __table_args__ = {
        "mysql_charset": "utf8"
    }