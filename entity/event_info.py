#引入要使用的declarative_base
from sqlalchemy.ext.declarative import declarative_base
#在要映射的数据表students中有id，name两个字段，所以要引入Integer对应id，String对应name
from sqlalchemy import Column, Integer, String,DateTime,CHAR
#声名Base
Base = declarative_base()
#User类就是对应于 __tablename__ 指向的表，也就是数据表students的映射
class EventInfo(Base):
#students表是我本地数据库testdab中已存在的
    __tablename__ = 'event_info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    event_type = Column(Integer)
    event_date=Column(Integer)
    event_location=Column(String(200))
    event_desc=Column(String(200))
    oldperson_id=Column(Integer)
    img_dir=Column(String(100))
    __table_args__ = {
        "mysql_charset": "utf8"
    }