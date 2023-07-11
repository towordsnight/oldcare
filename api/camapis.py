from time import time

from flask import Flask, Response, Blueprint, render_template
from camera.camrea import BaseCamera
from camera.video_stream import LoadStreams
import cv2
from flask_socketio import SocketIO, emit

# index = Blueprint("index", __name__, template_folder="templates")
index = Flask(__name__)
socketio = SocketIO()
socketio.init_app(index, cors_allowed_origins='*')
name_space = '/echo'

class Camera(BaseCamera):
    @staticmethod
    def frames():
        # 此处为自己的视频流url 格式 "rtsp://%s:%s@%s//Streaming/Channels/%d" % (name, pwd, ip, channel)
        # 例如
        # source = 'rtmp://8.130.83.55:1935/mylive'
        # source = 'rtsp://8.130.83.55:8554/live'
        source = '0'
        dataset = LoadStreams(source)
        for im0s in dataset:
            im0 = im0s[0].copy()
            frame = cv2.cvtColor(im0, cv2.COLOR_BGR2RGB)
            result = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            yield cv2.imencode('.jpg', result)[1].tobytes()


class Camera2(BaseCamera):
    @staticmethod
    def frames():
        # 此处为自己的视频流url 格式 "rtsp://%s:%s@%s//Streaming/Channels/%d" % (name, pwd, ip, channel)
        # 例如
        # source = 'rtmp://8.130.83.55:1935/mylive'
        source = 'rtsp://8.130.83.55:8554/live'
        # source = '0'
        dataset = LoadStreams(source)
        for im0s in dataset:
            im0 = im0s[0].copy()
            frame = cv2.cvtColor(im0, cv2.COLOR_BGR2RGB)
            result = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            yield cv2.imencode('.jpg', result)[1].tobytes()

@index.route('/')
def index_to():
    return render_template('test.html')


# <img src="{{url_for('cam/video_play')}}" class="img-fluid" height="500">

@index.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(genWeb(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@index.route('/video_feed_2')
def video_feed_2():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(genWeb(Camera2()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


def genWeb(camera):
    """Video streaming generator function."""

    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')



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


@index.route('/push')
def push_once():
    event_name = 'echo'
    broadcasted_data = {'data': "test message!"}
    # 设置广播数据
    socketio.emit(event_name, broadcasted_data, namespace=name_space)
    return 'done!'

@index.route('/pushs')
def pushs():
    event_name = 'echo'
    # 设置广播数据
    for i in range(100):
        socketio.emit(event_name, "broadcasted_data"+i, broadcast=False, namespace=name_space)
    return 'done!'



if __name__ == '__main__':
    socketio.run(index, host='0.0.0.0', port=5001)
