import time

from entity.Volunteer import Volunteer as VolunteerInfo
from config import sqlInit
from sqlalchemy.orm import sessionmaker
import logging
from datetime import datetime

Session = sessionmaker(bind=sqlInit.db)


def get_volunteer_info_by_id(id):
    session = Session()
    try:
        result = session.query(VolunteerInfo).filter(VolunteerInfo.volunteerID == id).first()
    except Exception as e:
        logging.error(e)
        return None
    session.close()
    return result


def get_volunteer_info_by_name(name):
    session = Session()
    try:
        result = session.query(VolunteerInfo).filter(VolunteerInfo.volunteerName == name).first()
    except Exception as e:
        logging.error(e)
        return None
    session.close()
    return result


def get_volunterr_info_list(page, pagesize, username):
    session = Session()
    try:
        if username == None:
            result = session.query(VolunteerInfo).filter().limit(pagesize).offset((page - 1) * pagesize).all()
        else:
            result = session.query(VolunteerInfo).filter(VolunteerInfo.volunteerName.like("%" + username + "%"),
                                                         VolunteerInfo.REMOVE == 0).limit(pagesize).offset(
                (page - 1) * pagesize).all()
    except Exception as e:
        logging.error(e)
        return None
    session.close()
    return result


def get_volunteer_checkin_count_by_day(today, tomorrow):
    session = Session()
    try:
        result = session.query(VolunteerInfo).filter(VolunteerInfo.checkin_date >= today,
                                                     VolunteerInfo.checkin_date <= tomorrow).count()
    except Exception as e:
        logging.error(e)
        return None
    session.close()
    return result


def get_volunteer_count_by_gender(sex):
    session = Session()
    try:
        result = session.query(VolunteerInfo).filter(VolunteerInfo.gender == sex).count()
    except Exception as e:
        logging.error(e)
        return None
    session.close()
    return result


def get_volunteer_checkout_count_by_day(today, tomorrow):
    session = Session()
    try:
        result = session.query(VolunteerInfo).filter(VolunteerInfo.checkout_date >= today,
                                                     VolunteerInfo.checkout_date <= tomorrow).count()
    except Exception as e:
        logging.error(e)
        return None
    session.close()
    return result


def add_volunteer_info(username, age, gender, phone, id_card, checkin_date, description, createby):
    session = Session()
    person = VolunteerInfo(volunteerName=username, age=age, gender=gender, phone=phone, id_card=id_card,
                           checkin_date=checkin_date, profile_photo=id_card + ".jpg", description=description,
                           createby=createby, created=time.localtime())
    p = None
    try:
        result = session.add(person)
        session.flush()
        p = sqlInit.query_to_dict(person)
        # session.query(VolunteerInfo).filter(VolunteerInfo.id==p.id).update({'imgset_dir':p.id,'profile_photo':p.id+".jpg"})
        session.commit()
    except Exception as e:
        logging.error(e)
        return None
    session.close()
    return p


def update_volunteer_info_by_id(id, username, gender, phone, id_card, birthday, checkin_date, checkout_date,
                                DESCRIPTION, UPDATEBY):
    session = Session()

    person = VolunteerInfo(volunteerID=id, volunteerName=username, gender=gender, phone=phone, id_card=id_card,
                           checkin_date=checkin_date, checkout_date=checkout_date, description=DESCRIPTION)
    try:
        u = person.__dict__
        u.pop("_sa_instance_state")
        row = session.query(VolunteerInfo).filter(VolunteerInfo.volunteerID == id).update(u)
        session.commit()
    except Exception as e:
        logging.error(e)
        return False
    session.close()
    return True


def delete_volunteer_info_by_id(id, UPDATEBY):
    session = Session()
    try:
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        session.query(VolunteerInfo).filter(VolunteerInfo.volunteerID == id).delete()
        session.commit()
    except Exception as e:
        logging.error(e)
        return False
    session.close()
    return True
