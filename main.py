# coding=UTF-8

from flask import Flask, render_template, request
from sqlalchemy import *
import flask_cors
from api.apis import index_page

app = Flask(__name__)
cors = flask_cors.CORS(app, resources={r"/*": {"origins": "*"}})
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/monitor'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# r=redisInit.get_connection()
# engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)
# 注册路由
app.register_blueprint(index_page, url_prefix="/user")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
