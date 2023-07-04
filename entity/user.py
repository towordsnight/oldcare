#引入要使用的declarative_base
from sqlalchemy.ext.declarative import declarative_base
#在要映射的数据表students中有id，name两个字段，所以要引入Integer对应id，String对应name
from sqlalchemy import Column, Integer, String,DateTime,CHAR
#声名Base
Base = declarative_base()
#User类就是对应于 __tablename__ 指向的表，也就是数据表students的映射
class User(Base):
#students表是我本地数据库testdab中已存在的
    __tablename__ = 'user'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50),nullable=False)
    password=Column(String(50))
    # REAL_NAME=Column(String(50))
    # SEX=Column(String(20))
    # EMAIL=Column(String(50))
    # PHONE=Column(String(50))
    # MOBILE=Column(String(50))
    # DESCRIPTION=Column(String(200))
    # ISACTIVE=Column(String(10))
    # CREATED=Column(DateTime)
    # CREATEBY=Column(Integer)
    # UPDATED=Column(DateTime)
    # UPDATEBY=Column(Integer)
    # REMOVE=Column(CHAR)

    __table_args__ = {
        "mysql_charset": "utf8"
    }