from flask import Flask, Response, Blueprint, render_template, current_app, request
from camera.camrea import BaseCamera
from camera.video_stream import LoadStreams
import cv2
import base64
from flask_socketio import SocketIO, emit
from threading import Lock, Thread
from collections import deque
from time import sleep

thread = None
thread_lock = Lock()
video_thread_lock = Lock()

# 本地摄像头
thread_video1 = None

# 事件线程
msg_thread = None

video_opend = False
"""
循环队列
"""


class CircularQueue:
    def __init__(self, max_size):
        self.queue = deque(maxlen=max_size)

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) == 0:
            raise IndexError("Queue is empty")
        return self.queue.popleft()

    def rotate(self, n):
        self.queue.rotate(n)

    def isNull(self):
        return len(self.queue)==0

"""视频帧队列"""
queue_img1 = CircularQueue(max_size=10)

"""视频帧队列"""
queue_img2 = CircularQueue(max_size=10)

"""事件消息队列"""
queue_event = CircularQueue(max_size=15)

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
            # frame = cv2.cvtColor(im0, cv2.COLOR_BGR2RGB)
            # result = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            # yield cv2.imencode('.jpg', frame)[1].tobytes()

            """
            使用socket传输照片时需要转为base64编码
            """
            frame = cv2.cvtColor(im0, cv2.COLOR_BGR2RGB)
            buffer = cv2.imencode('.jpg', frame)[1]
            yield base64.b64encode(buffer)


# <img src="{{url_for('cam/video_play')}}" class="img-fluid" height="500">
@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(genWeb(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def genWeb(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_locality_close')
def video_locality_close():
    global video_opend
    video_opend = True


@app.route('/video_locality')
def video_org():
    global thread_video1  # 全局变量thread
    with video_thread_lock:  # 该行实现了系统同时只能有一个连接，因为全局变量thread只有一个，确保当有两个客户端同时访问时不会对thread重复赋值
        print(video_thread1)
        if thread_video1 is None:
            # 如果socket连接，则开启一个线程，专门给前端发送消息
            thread_video1 = Thread(target=video_thread1, args=(Camera(),))
            thread_video1.start()

    return "thread start"



"""
本地摄像头线程，
这里生成图像并插入队列
"""
def video_thread1(camera):
    global video_opend
    """算法加载

    """
    while True:
        frame = camera.get_frame()
        queue_img1.enqueue(frame)
        sleep(0.03)
        if video_opend:
            break



@socketio.on('connect', namespace=name_space)
def test_connect():
    """
    此函数在建立socket连接时被调用
    """
    print("socket 建立连接")

    global thread    # 全局变量thread
    with app.app_context():
        with thread_lock:   # 该行实现了系统同时只能有一个连接，因为全局变量thread只有一个，确保当有两个客户端同时访问时不会对thread重复赋值
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
            # socketio.emit('server_response', "test", room=None, namespace=name_space)
            if not queue_img1.isNull():
                socketio.emit('img', queue_img1.dequeue(), room=None, namespace=name_space)
        socketio.sleep(0.03)


@socketio.on('disconnect', namespace=name_space)
def disconnect_msg():
    print('client disconnected.')


@socketio.on('server_response', namespace=name_space)
def mtest_message(message):
    print(message)
    emit('server_response', {'data': message['data'], 'count': 1})




if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5001)
