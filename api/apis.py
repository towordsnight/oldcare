
from flask import Flask, Blueprint, request, make_response, jsonify, session
from flask import request
import datetime
import jwt
from model.userService import *
from model.elderly_info import *
from model.volunteer_info import *

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

# 生成访问令牌
def generate_access_token(username):
    # 设置访问令牌的有效期
    expiry_time = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    # 构建访问令牌的载荷
    payload = {
        'username': username,
        'exp': expiry_time
    }
    # 使用密钥对载荷进行签名，生成访问令牌
    access_token = jwt.encode(payload, 'FFFbjtu', algorithm='HS256')
    return access_token

@index_page.route('/admin/login', methods=['POST'])
def admin_login():
    # 获取请求数据
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')


    # 进行管理员身份验证逻辑
    # 如果用户名和密码正确
    if is_existed(username, password):
        # 生成访问令牌
        access_token = generate_access_token(username)
        # 返回响应
        session['username'] = username
        # 构造响应数据
        response = {
            'status': 'success',
            'message': 'Login successful',
            'access_token': access_token
        }
        return jsonify(response), 200
    else:
        # 身份验证失败
        response = {
            'status': 'error',
            'message': 'Invalid username or password'
        }
        return jsonify(response), 401


@index_page.route('/admin/register', methods=['POST'])
def admin_register():
    # 获取请求数据
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    realn = data.get('realname')
    sex = data.get('sex')
    email = data.get('email')
    phone = data.get('phone')
    # 检查用户名是否已存在
    user = get_sys_user_by_username(username)
    # user = SysManager.query.filter_by(username=username).first()
    if user:
        response = {
            'status': 'error',
            'message': 'Username already exists'
        }
        return jsonify(response), 409

    # 将新用户的信息插入到数据库中
    if add_sys_user(username,password,realn,sex,email,phone):
        response = {
            'status': 'success',
            'message': 'Admin registered successfully'
        }
        return jsonify(response), 200

    response = {
        'status': 'error',
        'message': 'Username already exists'
    }
    return jsonify(response), 409



@index_page.route('/elderly', methods=['GET'])
def get_elderly_list():
    data = request.get_json()
    #根据elderlyName查询数据库中对应的所有信息
    elderly = get_old_person_info_by_name(data.get('elderlyName'))
    # 如果没有找到对应的老人信息
    if not elderly:
        response = {
            'status': 'error',
            'message': 'No elderly found'
        }
        return jsonify(response), 404
    # 如果找到了对应的老人信息
    else:
        # 构建响应数据
        # 展示该老人所有信息
        elderly_info = {
            'elderlyName': elderly.elderlyName,
            'age': elderly.age,
            'gender': elderly.gender,
            'id_card': elderly.id_card,
            'birthday': elderly.birthday,
            'checkin_date': elderly.checkin_date,
            'checkout_date': elderly.checkout_date,
            'address': elderly.address,
            'phone': elderly.phone,
            'imgset_dir': elderly.imgset_dir,
            'profile_photo': elderly.profile_photo,
            'room_number': elderly.room_number,
            'first_guardian_name': elderly.first_guardian_name,
            'first_guardian_relationship': elderly.first_guardian_relationship,
            'first_guardian_phone': elderly.first_guardian_phone,
            'second_guardian_name': elderly.second_guardian_name,
            'second_guardian_relationship': elderly.second_guardian_relationship,
            'second_guardian_phone': elderly.second_guardian_phone,
            'health_state': elderly.health_state,
            'description': elderly.description,
            'created': elderly.created,
            'createby': elderly.createby
        }
        response = {
            'status': 'success',
            'data': {
                'elderly': elderly_info
            }
        }
        return jsonify(response), 200

# 用列表存储老人信息
elderly_list = []
@index_page.route('/elderly/add-one', methods=['POST'])
def add_eld():
    data = request.get_json()
    added_elderlys = []
    for elderly_data in data:
        result = add_elderly(elderly_data)
        if 'error' in result:
            return jsonify({'error': result['error']}), 400
        added_elderlys.append(result)

    return {'msg': '添加成功', 'elderly': added_elderlys}

def add_elderly(data):
    # 必填字段
    required_fields = ['elderlyName', 'age', 'gender', 'id_card', 'first_guardian_name', 'first_guardian_phone', 'first_guardian_relationship']
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        return {'error': f'Missing required fields: {", ".join(missing_fields)}'}

    # 检查身份证号是否已存在
    ifelder = get_old_person_info_by_idcard(data['id_card'])
    if ifelder is not None:
        return {'error': 'The same idcard,Elderly already exists'}


    # 创建时间和创建人
    created = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # 从会话中获取当前用户信息
    username = session['username']
    # 如果会话中没有当前用户信息，则返回未登录错误
    if not username:
        return jsonify({'error': '用户未登录'}), 401
    createby = username

    # 添加到老人列表
    elderly = {
        'elderlyName': data['elderlyName'],
        'age': data.get('age'),
        'gender': data['gender'],
        'id_card': data['id_card'],
        'birthday': data.get('birthday'),
        'checkin_date': data.get('checkin_date'),
        'checkout_date': data.get('checkout_date'),
        'address': data.get('address'),
        'phone': data.get('phone'),
        'imgset_dir': data.get('imgset_dir'),
        'profile_photo': data.get('profile_photo'),
        'room_number': data.get('room_number'),
        'first_guardian_name': data['first_guardian_name'],
        'first_guardian_relationship': data.get('first_guardian_relationship'),
        'first_guardian_phone': data['first_guardian_phone'],
        'second_guardian_name': data.get('second_guardian_name'),
        'second_guardian_relationship': data.get('second_guardian_relationship'),
        'second_guardian_phone': data.get('second_guardian_phone'),
        'health_state': data.get('health_state'),
        'description': data.get('description'),
        'created': created,
        'createby': createby
    }
    if add_old_person(elderly):
        elderly_list.append(elderly)
        return elderly_list
    return jsonify({'error': '添加失败'}), 405



# 更新老人信息接口
@index_page.route('/elderly/<int:elderly_id>', methods=['PUT'])
def update_elderly(elderly_id):
    data = request.get_json()
    elderly = get_old_person_info_by_id(elderly_id)
    if elderly:
        if update_oldperson_info_by_id(elderly_id,data.get('elderlyName'),data.get('age'),data.get('gender'),data.get('phone'),
                                    data.get('id_card'),data.get('birthday'),data.get('checkin_date'),data.get('checkout_date'),
                                    data.get('address'),data.get('imgset_dir'),data.get('profile_photo'),data.get('room_number'),
                                    data.get('first_guardian_name'),data.get('first_guardian_relationship'),data.get('first_guardian_phone'),
                                    data.get('second_guardian_name'),data.get('second_guardian_relationship'),data.get('second_guardian_phone'),
                                    data.get('health_state'),data.get('description'),data.get('createby')
                                    ):
            return jsonify({'msg': '更新成功'})

    return jsonify({'error': '未找到该老人信息'}), 404


@index_page.route('/elderly/<int:elderly_id>', methods=['DELETE'])
def delete_elderly(elderly_id):
    elderly = get_old_person_info_by_id(elderly_id)
    if elderly:
        delete_elderly(elderly)
        return jsonify({'msg': '删除成功'})
    else:
        return jsonify({'error': '未找到该老人信息'}), 404


@index_page.route('/volunteer', methods=['GET'])
def get_volunteer():
    data = request.get_json()
    # 根据义工姓名查询数据库中对应的所有信息
    volunteer = get_volunteer_info_by_name(data.get('volunteerName'))

    # 如果没有找到对应的义工信息
    if not volunteer:
        response = {
            'status': 'error',
            'message': 'No volunteer found'
        }
        return jsonify(response), 404

    # 如果找到了对应的义工信息
    else:
        # 构建响应数据，展示该义工所有信息
        volunteer_info = {
            'volunteerName': volunteer.volunteerName,
            'age': volunteer.age,
            'gender': volunteer.gender,
            'id_card': volunteer.id_card,
            'checkin_date': volunteer.checkin_date,
            'checkout_date': volunteer.checkout_date,
            'phone': volunteer.phone,
            'imgset_dir': volunteer.imgset_dir,
            'profile_photo': volunteer.profile_photo,
            'description': volunteer.description,
            'created': volunteer.created,
            'createby': volunteer.createby
        }
        response = {
            'status': 'success',
            'data': {
                'volunteer': volunteer_info
            }
        }
        return jsonify(response), 200

@index_page.route('/volunteer/<int:volunteer_id>', methods=['DELETE'])
def delete_volunt(volunteer_id):
    volunteer = get_volunteer_info_by_id(volunteer_id)

    if volunteer:
        if delete_volunteer_info_by_id(volunteer_id):
            return jsonify({'msg': '删除成功'})

    return jsonify({'error': '未找到该义工信息'}), 404


@index_page.route('/volunteer/<int:volunteer_id>', methods=['PUT'])
def update_volunteer(volunteer_id):
    data = request.get_json()
    volunteer = get_volunteer_info_by_id(volunteer_id)

    if volunteer:
        if update_volunteer_info_by_id(volunteer_id,data.get('volunteerName'),data.get('gender'),data.get('age'),
                                    data.get('phone'),data.get('id_card'),data.get('checkin_date'),data.get('checkout_date'),
                                    data.get('description'),data.get('imgset_dir'),data.get('profile_photo'),data.get('createby')
                                    ):
            return jsonify({'msg': '更新成功'})

    return jsonify({'error': '更新失败'}), 404


# 使用列表存储义工信息
volunteer_list = []
# 添加义工接口
@index_page.route('/volunteer/add-one', methods=['POST'])
def add_volunt():
    data = request.get_json()
    added_volunteers = []
    for volunteer_data in data:
        result = add_volunteer(volunteer_data)
        if 'error' in result:
            return jsonify({'error': result['error']}), 400
        added_volunteers.append(result)

    return {'msg': '添加成功', 'volunteer': added_volunteers}


def add_volunteer(data):
    # 必填字段
    required_fields = ['volunteerName', 'age', 'gender', 'id_card', 'first_guardian_name', 'first_guardian_phone',
                       'first_guardian_relationship']
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        return {'error': f'Missing required fields: {", ".join(missing_fields)}'}

    # 检查身份证号是否已存在
    ifvolunteer = get_volunteer_info_by_idcard(data['id_card'])
    if ifvolunteer:
        return {'error': 'The same idcard, Volunteer already exists'}

    # 创建时间和创建人
    created = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # 从会话中获取当前用户信息
    username = session.get('username')
    # 如果会话中没有当前用户信息，则返回未登录错误
    if not username:
        return {'error': '用户未登录'}, 401
    createby = username

    # 添加到义工列表
    volunteer = {
        'volunteerName': data['volunteerName'],
        'age': data.get('age'),
        'gender': data['gender'],
        'id_card': data['id_card'],
        'checkin_date': data.get('checkin_date'),
        'checkout_date': data.get('checkout_date'),
        'phone': data.get('phone'),
        'imgset_dir': data.get('imgset_dir'),
        'profile_photo': data.get('profile_photo'),
        'description': data.get('description'),
        'created': created,
        'createby': createby
    }

    if add_volunteer(volunteer):
        volunteer_list.append(volunteer)
        return volunteer_list
    return {'error': 'operation failed'}




