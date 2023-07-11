from flask import Flask, Blueprint, jsonify
from flask import request
from model.event_info import *

event = Blueprint("event", __name__)


@event.route('/search', methods=['POST'])
def get_event():
    data = request.get_json()
    # 根据elderlyName查询数据库中对应的所有信息
    events = get_event_info_list(data.get('event_type'))
    # 如果没有找到对应的老人信息
    if events is None:
        response = {
            'error': '不存在',
        }
        return jsonify(response), 200

    events_list = []

    for event in events:
        event_info = {
            'eventID': event.eventID,
            'event_type': event.event_type,
            'event_start': event.event_start,
            'event_location': event.event_location,
            'oldperson_id': event.oldperson_id,
            'elderlyName': event.elderlyName
        }
        events_list.append(event_info)
    response = {
        'status': 'success',
        'data': events_list
    }
    return response


