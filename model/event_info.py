from entity.Event import Event as EventInfo
from config import sqlInit
from sqlalchemy.orm import sessionmaker
import logging
from datetime import datetime

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
    user = EventInfo(event_type=event_type, event_start=datetime.now(), event_location=event_location, oldperson_id=oldperson_id,
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
        q = q.filter(EventInfo.event_type == event_type).order_by(EventInfo.event_start.desc()).all()
    except Exception as e:
        logging.error(e)
        return None
    session.close()
    return q

