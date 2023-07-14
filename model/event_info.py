from sqlalchemy import func

from entity.Event import Event as EventInfo
from config import sqlInit
from sqlalchemy.orm import sessionmaker
import logging
from datetime import datetime, timedelta, date

Session = sessionmaker(bind=sqlInit.db)


def get_event_info_by_id(id):
    session = Session()
    try:
        result = session.query(EventInfo).filter(EventInfo.eventID == id).first()
        session.commit()
    except Exception as e:
        logging.error(e)
        return None
    session.close()
    return result


def add_event_info(event_type, event_location, oldperson_id, elderlyName):
    session = Session()
    user = EventInfo(event_type=event_type, event_start=datetime.now(), event_location=event_location,
                     oldperson_id=oldperson_id,
                     elderlyName=elderlyName
                     )
    print(user)
    try:
        result = session.add(user)
        session.commit()
    except Exception as e:
        logging.error(e)
        return False
    session.close()
    return True


def delete_old_person_info_by_id(id):
    session = Session()
    try:
        session.query(EventInfo).filter(EventInfo.eventID == id).delete()
        session.commit()
    except Exception as e:
        logging.error(e)
        return False
    session.close()
    return True


def get_event_info_list(event_type):
    session = Session()
    try:
        q = session.query(EventInfo)
        if event_type is None:
            q = q.filter().order_by(EventInfo.event_start.desc()).all()
        else:
            q = q.filter(EventInfo.event_type.like("%" + event_type + "%")).order_by(EventInfo.event_start.desc()).all()
    except Exception as e:
        logging.error(e)
        return None
    session.close()
    return q


def get_event_info_bydate(event_start):
    session = Session()
    try:
        q = session.query(EventInfo)
        if event_start is None:
            q = q.filter().order_by(EventInfo.event_start.desc()).all()
        else:
            time1 = datetime.strptime(event_start, '%Y-%m-%d').date()

            q = q.filter(func.date(EventInfo.event_start) == time1).order_by(EventInfo.event_start.desc()).all()
    except Exception as e:
        logging.error(e)
        return None
    session.close()
    return q
