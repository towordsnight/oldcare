from flask import Flask, Response, Blueprint, render_template, current_app, request
from camera.camrea import BaseCamera
from camera.video_stream import LoadStreams
import cv2
from flask_socketio import SocketIO, emit
from threading import Lock,Thread



thread = None
thread_lock = Lock()


# index = Blueprint("index", __name__, template_folder="templates")
app = Flask(__name__)
socketio = SocketIO()
socketio.init_app(app, cors_allowed_origins='*')
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

@app.route('/')
def index_to():
    return render_template('test.html')


# <img src="{{url_for('cam/video_play')}}" class="img-fluid" height="500">

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(genWeb(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_2')
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
def test_connect():
    """
    此函数在建立socket连接时被调用
    """
    print("socket 建立连接")
    global thread
    with app.app_context():
        with thread_lock:
            print(thread)
            if thread is None:
                # 如果socket连接，则开启一个线程，专门给前端发送消息
                thread = socketio.start_background_task(target=background_thread)

def background_thread():
    """
    该线程专门用来给前端发送消息
    :return:
    """
    while True:
        """这里传递事件的信息"""
        """一旦建立连接线程一直存在"""
        with app.app_context():
            socketio.emit('server_response', "test", room=None, namespace=name_space)
        socketio.sleep(1)



@socketio.on('disconnect', namespace=name_space)
def disconnect_msg():
    print('client disconnected.')

@socketio.on('server_response', namespace=name_space)
def mtest_message(message):
    print(message)
    emit('server_response', {'data': message['data'], 'count': 1})





if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5001)
