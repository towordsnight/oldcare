from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Date,CHAR



Base = declarative_base()



class Volunteer(Base):
    __tablename__ = 'volunteer'

    volunteerID = Column(Integer, primary_key=True)
    volunteerName = Column(String(20), nullable=False)
    age = Column(Integer)
    gender = Column(String(20))
    id_card = Column(String(20))
    checkin_date = Column(Date)
    checkout_date = Column(Date)
    phone = Column(String(20))
    profile_photo = Column(String(collation='utf8_general_ci'))
    description = Column(String(50))
    created = Column(Date)
    createby = Column(String(20))
    __table_args__ = {
        "mysql_charset": "utf8"
    }