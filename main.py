# coding=UTF-8

from flask import Flask, render_template, request
import flask_cors
from api.apis import index_page
from api.camapis import index


app = Flask(__name__)
cors = flask_cors.CORS(app, resources={r"/*": {"origins": "*"}})
app.register_blueprint(index_page)
app.register_blueprint(index, url_prefix="/cam")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
    # server = pywsgi.WSGIServer(('127.0.0.1', 5000), index_page)
    # server.serve_forever()
