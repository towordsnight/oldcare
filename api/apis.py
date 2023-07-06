
from flask import Flask, Blueprint, request, make_response, jsonify, render_template
from flask import redirect
from flask import url_for
from gevent import pywsgi
from flask import request
from model.userService import *


index_page = Blueprint("index_page", __name__)


def make_success_response(data,message):
    response={}
    response['code']='success'
    response['message']=message
    response['data']=data
    return response
def make_error_response(data,messsage):
    response={}
    response['code']='error'
    response['message']=messsage
    response['data']=data
    return response


@index_page.route("/text_same")
def text_same():
    response = make_response("templates/test.html", 200)
    return response


@index_page.route("/json")
def json():
    import json
    data = {"a": "b"}
    response = make_response(json.dumps(data))
    response.headers["Content-Type"] = "application/json"
    return response


@index_page.route("/json_same")
def json_same():
    data = {"a": "b"}
    response = make_response(jsonify(data))
    return response

@index_page.route('/')
def hello_world():
    return 'Hello World?'


# @app.route('/')
# def index():
#     return redirect(url_for('user_login'))

@index_page.route('/login',methods=['GET','POST'])
def user_login():
    if request.method=='POST':  # 注册发送的请求为POST请求
        username = request.form['username']
        password = request.form['password']
        if is_null(username,password):
            login_massage = "温馨提示：账号和密码是必填"
            return login_massage
            # return render_template('login.html', message=login_massage)
        elif is_existed(username, password):
            return "success"
            # return render_template('index.html', username=username)
        elif get_sys_user_by_username(username):
            login_massage = "温馨提示：密码错误，请输入正确密码"
            return login_massage
            # return render_template('login.html', message=login_massage)
        else:
            login_massage = "温馨提示：不存在该用户，请先注册"
            return login_massage
            # return render_template('login.html', message=login_massage)
    # return render_template('login.html')
#
# @app.route("/regiser",methods=["GET", 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         if is_null(username,password):
#             login_massage = "温馨提示：账号和密码是必填"
#             return render_template('register.html', message=login_massage)
#         elif exist_user(username):
#             login_massage = "温馨提示：用户已存在，请直接登录"
#             # return redirect(url_for('user_login'))
#             return render_template('register.html', message=login_massage)
#         else:
#             add_user(request.form['username'], request.form['password'] )
#             return render_template('index.html', username=username)
#     return render_template('register.html')





# if __name__ == '__main__':
#     server = pywsgi.WSGIServer(('127.0.0.1', 5000), index_page)
#     server.serve_forever()
    # app.debug = True
    # app.run()
    # app.run(debug = True)
