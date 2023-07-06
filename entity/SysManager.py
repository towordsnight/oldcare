#引入要使用的declarative_base
from sqlalchemy.ext.declarative import declarative_base
#在要映射的数据表students中有id，name两个字段，所以要引入Integer对应id，String对应name
from sqlalchemy import Column, Integer, String,DateTime,CHAR


#声名Base
Base = declarative_base()



class SysManager(Base):
    __tablename__ = 'sys_manager'

    userID = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    psw = Column(String(20), nullable=False)
    realname = Column(String(20))
    sex = Column(String(4))
    email = Column(String(20))
    phone = Column(String(20))
    __table_args__ = {
        "mysql_charset": "utf8"
    }