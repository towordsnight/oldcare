from flask import Flask, Blueprint, jsonify
from flask import request
from datetime import datetime
from model.event_info import *
from flask_socketio import SocketIO, emit

# event = Blueprint("event", __name__)
event = Flask(__name__)
socketio = SocketIO()
socketio.init_app(event, cors_allowed_origins='*')
name_space = '/echo'

@event.route('/add', methods=['POST'])
def add_event():
    data = request.get_json()
    if add_event_info(data.get('event_type'), data.get('event_start'),
                      data.get('event_location'), data.get('oldperson_id')):
        return {'status': 'success'}
    return {'status': 'error'}


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


@event.route('/push')
def push_once():
    event_name = 'echo'
    broadcasted_data = {'data': "test message!"}
    # 设置广播数据
    socketio.emit(event_name, broadcasted_data, broadcast=False, namespace=name_space)
    return 'done!'

@event.route('/pushs')
def pushs():
    event_name = 'echo'
    # 设置广播数据
    for i in range(100):
        socketio.emit(event_name, "broadcasted_data"+i, broadcast=False, namespace=name_space)
    return 'done!'


@socketio.on('connect', namespace=name_space)
def connected_msg():
    print('client connected.')

@socketio.on('disconnect', namespace=name_space)
def disconnect_msg():
    print('client disconnected.')

@socketio.on('my_event', namespace=name_space)
def mtest_message(message):
    print(message)
    emit('my_response', {'data': message['data'], 'count': 1})

if __name__ == '__main__':
    socketio.run(event, host='0.0.0.0', port=5000)