from entity.Event import Event as EventInfo
from config import sqlInit
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
import logging
Session = sessionmaker(bind=sqlInit.db)
def get_event_info_by_id(id):
    session = Session()
    try:
        result = session.query(EventInfo).filter(EventInfo.id==id).first()
        session.commit()
    except Exception as e:
        logging.error(e)
        return None
    session.close()
    return result

def add_event_info(event_type,event_date,event_location,event_desc,oldperson_id,img_dir):
    session = Session()
    user=EventInfo(event_type=event_type,event_date=event_date,event_location=event_location,event_desc=event_desc,oldperson_id=oldperson_id,img_dir=img_dir)
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
        session.query(EventInfo).filter(EventInfo.id==id).delete()
        session.commit()
    except Exception as e:
        logging.error(e)
        return False
    session.close()
    return True

def get_event_info_list(page,pagesize,criteria):
    session = Session()
    try:
        q=session.query(EventInfo)
        if 'event_type' in criteria:
            q=q.filter(EventInfo.event_type==criteria['event_type'])
        if 'event_date' in criteria:
            q=q.filter(func.date_format(criteria['event_date'], "%Y-%m-%d")==func.date_format(EventInfo.event_date, "%Y-%m-%d"))
        if 'event_location' in criteria:
            q=q.filter(EventInfo.event_location.like("%"+criteria['event_location']+"%"))
        if 'event_desc' in criteria:
            q=q.filter(EventInfo.event_location.like("%"+criteria['event_desc']+"%"))
        if 'oldperson_id' in criteria:
            q=q.filter(EventInfo.oldperson_id==criteria['oldperson_id'])
        result = q.order_by(EventInfo.event_date.desc()).limit(pagesize).offset((page-1)*pagesize).all()
    except Exception as e:
        logging.error(e)
        return None
    session.close()
    return result

def get_event_info_count(criteria):
    session = Session()
    try:
        q=session.query(EventInfo)
        if 'event_type' in criteria:
            q=q.filter(EventInfo.event_type==criteria['event_type'])
        if 'event_date' in criteria:
            q=q.filter(func.date_format(criteria['event_date'], "%Y-%m-%d")==func.date_format(EventInfo.event_date, "%Y-%m-%d"))
        if 'event_location' in criteria:
            q=q.filter(EventInfo.event_location.like("%"+criteria['event_location']+"%"))
        if 'event_desc' in criteria:
            q=q.filter(EventInfo.event_location.like("%"+criteria['event_desc']+"%"))
        if 'oldperson_id' in criteria:
            q=q.filter(EventInfo.oldperson_id==criteria['oldperson_id'])
        result = q.count()
    except Exception as e:
        logging.error(e)
        return None
    session.close()
    return result