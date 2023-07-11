from flask import Flask
import flask_cors
from api.apis import index_page
from api.camapis import index
from api.upload import upload
from api.eventapi import event

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
cors = flask_cors.CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(index_page)
app.register_blueprint(upload, url_prefix="/upload")
app.register_blueprint(event, url_prefix="/event")



if __name__ == '__main__':
    # socketio.run(app, host='0.0.0.0', port=5000)
    app.run(host='0.0.0.0', port='5000', debug=True)

    # socketio.run(app, host='0.0.0.0', port=8088)
    # server = pywsgi.WSGIServer(('127.0.0.1', 5000), index_page)
    # server.serve_forever()

# @socketio.on('connect')
# def connected_msg():
#     print('client connected.')
#
# @socketio.on('disconnect')
# def disconnect_msg():
#     print('client disconnected.')