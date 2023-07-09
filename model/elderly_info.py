import time

from entity.Elderly import Elderly as OldPersonInfo
from config import sqlInit
from sqlalchemy.orm import sessionmaker
import logging

Session = sessionmaker(bind=sqlInit.db)


def get_old_person_info_by_id(id):
    session = Session()
    try:
        result = session.query(OldPersonInfo).filter(OldPersonInfo.elderlyID == id).all()
    except Exception as e:
        logging.error(e)
        return None
    session.close()
    return result

def get_old_person_info_by_idcard(idcard):
    session = Session()
    try:
        result = session.query(OldPersonInfo).filter(OldPersonInfo.id_card == idcard).all()
    except Exception as e:
        logging.error(e)
        return None
    session.close()
    return result


def get_old_person_info_by_name(username):
    session = Session()
    try:
        result = session.query(OldPersonInfo).filter(OldPersonInfo.elderlyName == username).first()
    except Exception as e:
        logging.error(e)
        return None
    session.close()
    return result

def get_old_person_infoall():
    session = Session()
    try:
        result = session.query(OldPersonInfo).filter().all()
    except Exception as e:
        logging.error(e)
        return None
    session.close()
    return result


def get_old_person_info_list(page, pagesize, username):
    session = Session()
    try:
        if username == None:
            result = session.query(OldPersonInfo).filter().limit(pagesize).offset((page - 1) * pagesize).all()
        else:
            result = session.query(OldPersonInfo).filter(OldPersonInfo.elderlyName.like("%" + username + "%")).limit(
                pagesize).offset(
                (page - 1) * pagesize).all()
    except Exception as e:
        logging.error(e)
        return None
    session.close()
    return result


def get_old_person_info_count(content):
    session = Session()
    try:
        if content == None:
            result = session.query(OldPersonInfo).filter().count()
        else:
            result = session.query(OldPersonInfo).filter(OldPersonInfo.elderlyName.like("%" + content + "%")).count()
    except Exception as e:
        logging.error(e)
        return None
    session.close()
    return result


def get_old_person_info_count_by_id(content):
    session = Session()
    try:
        if content == None:
            result = session.query(OldPersonInfo).count()
        else:
            result = session.query(OldPersonInfo).filter(OldPersonInfo.elderlyID == content).count()
    except Exception as e:
        logging.error(e)
        return None
    session.close()
    return result


def get_old_person_checkin_count_by_day(today, tomorrow):
    session = Session()
    try:
        result = session.query(OldPersonInfo).filter(OldPersonInfo.checkin_date >= today,
                                                     OldPersonInfo.checkin_date <= tomorrow).count()
    except Exception as e:
        logging.error(e)
        return None
    session.close()
    return result


def get_old_person_count_by_gender(sex):
    session = Session()
    try:
        result = session.query(OldPersonInfo).filter(OldPersonInfo.gender == sex).count()
    except Exception as e:
        logging.error(e)
        return None
    session.close()
    return result


def get_old_person_checkout_count_by_day(today, tomorrow):
    session = Session()
    try:
        result = session.query(OldPersonInfo).filter(OldPersonInfo.checkout_date >= today,
                                                     OldPersonInfo.checkout_date <= tomorrow).count()
    except Exception as e:
        logging.error(e)
        return None
    session.close()
    return result


def add_old_person_info(username, age, gender, phone, id_card, birthday, checkin_date, checkout_date,
                        address, imgset_dir,
                        profile_photo, room_number,
                        firstguardian_name, firstguardian_relationship, firstguardian_phone,
                        secondguardian_name, secondguardian_relationship, secondguardian_phone,
                        health_state, DESCRIPTION, CREATEBY):
    session = Session()
    person = OldPersonInfo(elderlyName=username, age=age, gender=gender, phone=phone, id_card=id_card, birthday=birthday,
                           checkin_date=checkin_date, checkout_date=checkout_date, imgset_dir=imgset_dir, address=address,
                           profile_photo=profile_photo,room_number=room_number,
                           first_guardian_name=firstguardian_name,
                           first_guardian_phone=firstguardian_phone,
                           first_guardian_relationship=firstguardian_relationship,
                           second_guardian_name=secondguardian_name,
                           second_guardian_relationship=secondguardian_relationship,
                           second_guardian_phone=secondguardian_phone,
                           health_state=health_state, created=time.localtime(),
                           description=DESCRIPTION, createby=CREATEBY)
    p = {}
    try:
        result = session.add(person)
        session.flush()
        p = sqlInit.query_to_dict(person)
        # session.query(OldPersonInfo).filter(OldPersonInfo.id==p.id).update({'imgset_dir':p.id,'profile_photo':p.id+".jpg"})
        session.commit()
    except Exception as e:
        logging.error(e)
        return None
    session.close()
    return p

def add_old_person(OldPersonInfo):
    session = Session()
    p = {}
    try:
        result = session.add(OldPersonInfo)
        session.flush()
        p = sqlInit.query_to_dict(OldPersonInfo)
        # session.query(OldPersonInfo).filter(OldPersonInfo.id==p.id).update({'imgset_dir':p.id,'profile_photo':p.id+".jpg"})
        session.commit()
    except Exception as e:
        logging.error(e)
        return False
    session.close()
    return True


def update_oldperson_info_by_id(ID, username, age, gender, phone, id_card, birthday, checkin_date, checkout_date,
                                address, imgset_dir,
                                profile_photo, room_number,
                                firstguardian_name, firstguardian_relationship, firstguardian_phone,
                                secondguardian_name, secondguardian_relationship, secondguardian_phone,
                                health_state, DESCRIPTION, CREATEBY):
    session = Session()

    person = OldPersonInfo()

    if username is not None:
        person.elderlyName = username
    if age is not None:
        person.age = username
    if gender is not None:
        person.gender = username
    if phone is not None:
        person.phone = username
    if id_card is not None:
        person.id_card = username
    if birthday is not None:
        person.birthday = username
    if checkin_date is not None:
        person.checkin_date = username
    if checkout_date is not None:
        person.checkout_date = username
    if address is not None:
        person.address = username
    if imgset_dir is not None:
        person.imgset_dir = username
    if profile_photo is not None:
        person.profile_photo = username
    if room_number is not None:
        person.room_number = username
    if firstguardian_name is not None:
        person.firstguardian_name = username
    if firstguardian_relationship is not None:
        person.firstguardian_relationship = username
    if firstguardian_phone is not None:
        person.firstguardian_phone = username
    if secondguardian_name is not None:
        person.secondguardian_name = username
    if secondguardian_relationship is not None:
        person.secondguardian_relationship = username
    if secondguardian_phone is not None:
        person.secondguardian_phone = username
    if health_state is not None:
        person.health_state = username
    if DESCRIPTION is not None:
        person.description = username
    if CREATEBY is not None:
        person.createby = username
    person.created = time.localtime()
    try:
        u = person.__dict__
        u.pop("_sa_instance_state")
        row = session.query(OldPersonInfo).filter(OldPersonInfo.elderlyID == ID).update(u)
        session.commit()
    except Exception as e:
        logging.error(e)
        return False
    session.close()
    return True


def delete_old_person_info_by_id(id):
    session = Session()
    try:
        session.query(OldPersonInfo).filter(OldPersonInfo.elderlyID == id).delete()
        session.commit()
    except Exception as e:
        logging.error(e)
        return False
    session.close()
    return True




if __name__ == '__main__':
    add_old_person_info("iaven",48,"xj","456","None",time.localtime(),time.localtime(),time.localtime(),None,None,None,"None","None","None","None","None","None","None",None,None,None)