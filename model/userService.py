from entity.SysManager import SysManager as User
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
        result = session.query(User).filter(User.username == username, User.psw == password).first()
    except Exception as e:
        logging.error(e)
        return False
    session.close()
    return result is not None


def get_sys_user_by_id(id):
    session = Session()
    try:
        result = session.query(User).filter(User.userID == id).first()
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
                                                User.realname.like("%" + name + "%"))).count()
    except Exception as e:
        logging.error(e)
        return None
    session.close()
    return result


def get_sys_user_count_by_gender(sex):
    session = Session()
    try:
        result = session.query(User).filter(User.sex == sex).count()
    except Exception as e:
        logging.error(e)
        return None
    session.close()
    return result


def get_sys_user_info_list(name):
    session = Session()
    try:
        if name == None:
            result = session.query(User).filter().all()
        else:
            result = session.query(User).filter(or_(User.username.like("%" + name + "%"),
                                                    User.realname.like("%" + name + "%"))).all()
    except Exception as e:
        logging.error(e)
        return None
    session.close()
    return result


def add_sys_user(username, psw, REAL_NAME, SEX, EMAIL, PHONE):
    session = Session()
    user = User(username=username, psw=psw, realname=REAL_NAME, sex=SEX, email=EMAIL, phone=PHONE)
    try:
        result = session.add(user)
        session.commit()
    except Exception as e:
        logging.error(e)
        return False
    session.close()
    return True


def update_sys_user_by_id(id, username, REAL_NAME, SEX, EMAIL,
                          PHONE):
    session = Session()

    user = User()
    if id is not None:
        user.userID = id
    if username is not None:
        user.username = username
    if REAL_NAME is not None:
        user.realname = REAL_NAME
    if SEX is not None:
        user.sex = SEX
    if EMAIL is not None:
        user.email = EMAIL
    if PHONE is not None:
        user.phone = PHONE
    try:
        u = user.__dict__
        u.pop("_sa_instance_state")
        row = session.query(User).filter(User.userID == id).update(u)
        session.commit()
    except Exception as e:
        logging.error(e)
        return False
    session.close()
    return True


def update_sys_user_password_by_id(id, old_password, new_password):
    session = Session()
    try:
        password = session.query(User).filter(User.userID == id).first()
        if password.psw != old_password:
            return 1
        row = session.query(User).filter(User.userID == id).update({'psw': new_password})
        session.commit()
    except Exception as e:
        logging.error(e)
        return 2
    session.close()
    return 0


def delete_sys_info_by_id(id):
    session = Session()
    try:
        session.query(User).filter(User.userID == id).delete()
        session.commit()
    except Exception as e:
        logging.error(e)
        return False
    session.close()
    return True


# if __name__ == '__main__':
#     update_sys_user_by_id(1, "fbf", "iaven", "male", "1245", "153")
