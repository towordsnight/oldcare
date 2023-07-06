from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,DateTime,CHAR



Base = declarative_base()

class Elderly(Base):
    __tablename__ = 'elderly'

    elderlyID = Column(Integer, primary_key=True)
    elderlyName = Column(String(20), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(20), nullable=False)
    id_card = Column(String(20), nullable=False)
    birthday = Column(DateTime)
    checkin_date = Column(DateTime)
    checkout_date = Column(DateTime)
    address = Column(String(20))
    phone = Column(String(20))
    imgset_dir = Column(String(200))
    profile_photo = Column(String(200))
    room_number = Column(String(20))
    first_guardian_name = Column(String(20), nullable=False)
    first_guardian_relationship = Column(String(20))
    first_guardian_phone = Column(String(20), nullable=False)
    second_guardian_name = Column(String(20))
    second_guardian_relationship = Column(String(20))
    second_guardian_phone = Column(String(20))
    health_state = Column(String(20))
    description = Column(String(50))
    created = Column(DateTime)
    createby = Column(String(20))
    __table_args__ = {
        "mysql_charset": "utf8"
    }