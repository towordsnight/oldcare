from entity.SysManager import User
from config import sqlInit
from sqlalchemy.orm import sessionmaker
import logging
from sqlalchemy import or_


Session = sessionmaker(bind=sqlInit.db)


def is_null(username, password):
    if username == '' or password == '':
        return True
    else:
        return False


def is_existed(username, password):
    session = Session()
    try:
        result = session.query(User).filter(User.username==username,User.password==password).first()
    except Exception as e:
        logging.error(e)
        return False
    session.close()
    return result is not None


def get_sys_user_by_id(id):
    session = Session()
    try:
        result = session.query(User).filter(User.ID == id).first()
    except Exception as e:
        logging.error(e)
        return None
    session.close()
    return result


def get_sys_user_by_username(username):
    session = Session()
    try:
        result = session.query(User).filter(User.username == username).first()
    except Exception as e:
        logging.error(e)
        return None
    session.close()
    return result


def get_sys_user_count(name):
    session = Session()
    try:
        result = session.query(User).filter(or_(User.username.like("%" + name + "%"),
                                                User.REAL_NAME.like("%" + name + "%"))).count()
    except Exception as e:
        logging.error(e)
        return None
    session.close()
    return result


def get_sys_user_count_by_gender(sex):
    session = Session()
    try:
        result = session.query(User).filter(User.SEX == sex, User.REMOVE == 0).count()
    except Exception as e:
        logging.error(e)
        return None
    session.close()
    return result


def get_sys_user_info_list(page, pagesize, name):
    session = Session()
    try:
        result = session.query(User).filter(or_(User.username.like("%" + name + "%"),
                                                User.REAL_NAME.like("%" + name + "%"))).limit(pagesize).offset(
            (page - 1) * pagesize).all()
    except Exception as e:
        logging.error(e)
        return None
    session.close()
    return result


def add_sys_user(username, password, REAL_NAME, SEX, EMAIL,
                 PHONE, MOBILE, DESCRIPTION, ISACTIVE, CREATEBY,
                 REMOVE):
    session = Session()
    user = User(username=username, password=password, REAL_NAME=REAL_NAME, SEX=SEX, EMAIL=EMAIL, PHONE=PHONE,
                MOBILE=MOBILE,
                DESCRIPTION=DESCRIPTION, ISACTIVE=ISACTIVE, CREATEBY=CREATEBY, REMOVE=REMOVE)
    try:
        result = session.add(user)
        session.commit()
        this = session.query(User).filter(User.username == username).first()
        session.query(User).filter(User.username == username).update({'CREATEBY': this.ID, 'UPDATEBY': this.ID})
        session.commit()
    except Exception as e:
        logging.error(e)
        return False
    session.close()
    return True


def update_sys_user_by_id(id, username, REAL_NAME, SEX, EMAIL,
                          PHONE, MOBILE, DESCRIPTION, ISACTIVE, UPDATEBY,
                          REMOVE):
    session = Session()

    user = User(ID=id, username=username, REAL_NAME=REAL_NAME, SEX=SEX, EMAIL=EMAIL, PHONE=PHONE, MOBILE=MOBILE,
                DESCRIPTION=DESCRIPTION, ISACTIVE=ISACTIVE, UPDATEBY=id, REMOVE=REMOVE)
    try:
        u = user.__dict__
        u.pop("_sa_instance_state")
        row = session.query(User).filter(User.ID == id).update(u)
        session.commit()
    except Exception as e:
        logging.error(e)
        return False
    session.close()
    return True


def update_sys_user_password_by_id(id, old_password, new_password):
    session = Session()
    try:
        password = session.query(User).filter(User.ID == id).first()
        if password.password != old_password:
            return 1
        row = session.query(User).filter(User.ID == id).update({'password': new_password})
        session.commit()
    except Exception as e:
        logging.error(e)
        return 2
    session.close()
    return 0


def delete_old_person_info_by_id(id):
    session = Session()
    try:
        session.query(User).filter(User.ID == id).delete()
        session.commit()
    except Exception as e:
        logging.error(e)
        return False
    session.close()
    return True
