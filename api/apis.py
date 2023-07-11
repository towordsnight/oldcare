from flask import Flask, Blueprint, request, make_response, jsonify, session
from flask import request
import datetime
from datetime import timedelta
import jwt
from model.userService import *
from model.elderly_info import *
from model.volunteer_info import *
from entity.Elderly import Elderly

index_page = Blueprint("index_page", __name__)


@index_page.route('/test', methods=['GET'])
def gettest():
    return "test"

# 生成访问令牌
def generate_access_token(username):
    # 设置访问令牌的有效期
    expiry_time = datetime.utcnow() + timedelta(hours=1)
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
        # session['username'] = username
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
        return jsonify(response), 200


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
    if add_sys_user(username, password, realn, sex, email, phone):
        response = {
            'status': 'success',
            'message': 'Admin registered successfully'
        }
        return jsonify(response), 200

    response = {
        'status': 'error',
        'message': '注册失败'
    }
    return jsonify(response), 409


@index_page.route('/admin/getlist_like', methods=['POST'])
def admin_listlike():
    user_list = []
    data = request.get_json()
    users = get_sys_user_info_list(data.get("username"))
    # 如果没有找到对应的老人信息
    if users is None:
        response = {
            'error': '不存在',
        }
        return jsonify(response), 200

    for user in users:
        user_info = {
            'userID': user.userID,
            'username': user.username,
            'realname': user.realname,
            'sex': user.sex,
            'email': user.email,
            'phone': user.phone
        }
        user_list.append(user_info)
    response = {
        'status': 'success',
        'data': user_list
    }
    return response

@index_page.route('/admin/update/<int:userid>', methods=['POST'])
def admin_update(userid):
    data = request.get_json()
    user = get_sys_user_by_id(userid)
    if user:
        if update_sys_user_by_id(userid,data.get("username"),data.get("realname"),data.get("sex"),
                                 data.get("email"), data.get("phone")) is not None:
            return jsonify({'msg': '更新成功'})

    return jsonify({'error': '未找到管理员信息'}), 404


@index_page.route('/admin/<int:userid>', methods=['DELETE'])
def delete_user(userid):
    user = get_sys_user_by_id(userid)
    if user:
        if delete_sys_info_by_id(userid):
            return jsonify({'msg': '删除成功'})
        return jsonify({'error': '删除失败'}), 410
    else:
        return jsonify({'error': '未找到管理员信息'}), 404





@index_page.route('/elderly', methods=['POST'])
def get_elderly_byname():
    data = request.get_json()
    # 根据elderlyName查询数据库中对应的所有信息
    elderly = get_old_person_info_by_name(data.get('elderlyName'))
    print(data.get('elderlyName'))
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
            'elderlyID': elderly.elderlyID,
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


@index_page.route('/elderly_namelike', methods=['POST'])
def get_old_person_info():
    data = request.get_json()
    # 根据elderlyName查询数据库中对应的所有信息
    elderlys = get_old_person_info_list(data.get('elderlyName'))
    # 如果没有找到对应的老人信息
    if elderlys is None:
        response = {
            'error': '不存在',
        }
        return jsonify(response), 200

    elderlys_list = []

    for elderly in elderlys:
        elderly_info = {
            'elderlyID': elderly.elderlyID,
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
        elderlys_list.append(elderly_info)
    response = {
        'status': 'success',
        'data': elderlys_list
    }
    return response


@index_page.route('/all_elderly', methods=['GET'])
def get_elderly_list():
    elderlys_list = []

    elderlys = get_old_person_infoall()
    for elderly in elderlys:
        elderly_info = {
            'elderlyID': elderly.elderlyID,
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
        elderlys_list.append(elderly_info)
    response = {
        'status': 'success',
        'data': {
            'elderly': elderlys_list
        }
    }
    return response


# 用列表存储老人信息
elderly_list = []


@index_page.route('/elderly/add-one', methods=['POST'])
def add_eld():
    data = request.get_json()
    if add_old_person_info(data.get('elderlyName'), data.get('age'), data.get('gender'), data.get('phone'),
                           data.get('id_card'),
                           data.get('birthday'), data.get('checkin_date'), data.get('checkout_date'),
                           data.get('address'),
                           data.get('imgset_dir'), data.get('profile_photo'), data.get('room_number'),
                           data.get('first_guardian_name'), data.get('first_guardian_relationship'),
                           data.get('first_guardian_phone'),
                           data.get('second_guardian_name'), data.get('second_guardian_relationship'),
                           data.get('second_guardian_phone'),
                           data.get('health_state'), data.get('description'), data.get('createby')
                           ) is not None:
        return {'status': 'success'}
    return {'status': 'error'}


# 更新老人信息接口
@index_page.route('/elderly_update/<int:elderly_id>', methods=['POST'])
def update_elderly(elderly_id):
    data = request.get_json()

    elderly = get_old_person_info_by_id(elderly_id)
    if elderly:
        if update_oldperson_info_by_id(elderly_id, data.get('elderlyName'), data.get('age'), data.get('gender'),
                                       data.get('phone'),
                                       data.get('id_card'), data.get('birthday'), data.get('checkin_date'),
                                       data.get('checkout_date'),
                                       data.get('address'), data.get('imgset_dir'), data.get('profile_photo'),
                                       data.get('room_number'),
                                       data.get('first_guardian_name'), data.get('first_guardian_relationship'),
                                       data.get('first_guardian_phone'),
                                       data.get('second_guardian_name'), data.get('second_guardian_relationship'),
                                       data.get('second_guardian_phone'),
                                       data.get('health_state'), data.get('description'), data.get('createby')
                                       ) is not None:
            return jsonify({'msg': '更新成功'})

    return jsonify({'error': '未找到该老人信息'}), 404


@index_page.route('/elderly_delete/<int:elderly_id>', methods=['DELETE'])
def delete_elderly(elderly_id):
    elderly = get_old_person_info_by_id(elderly_id)
    if elderly:
        if delete_old_person_info_by_id(elderly_id):
            return jsonify({'msg': '删除成功'})
        return jsonify({'error': '删除失败'}), 410
    else:
        return jsonify({'error': '未找到该老人信息'}), 404


@index_page.route('/volunteer', methods=['POST'])
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


@index_page.route('/volunteerlike', methods=['POST'])
def get_vollike():
    data = request.get_json()
    # 根据elderlyName查询数据库中对应的所有信息
    vols = get_volunterr_info_list(data.get('volunteerName'))
    # 如果没有找到对应的老人信息
    if vols is None:
        response = {
            'error': '不存在',
        }
        return jsonify(response), 200

    vols_list = []

    for volunteer in vols:
        volunteer_info = {
            'volunteerID': volunteer.volunteerID,
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
        vols_list.append(volunteer_info)
    response = {
        'status': 'success',
        'data': vols_list
    }
    return response


@index_page.route('/volunteer_delete/<int:volunteer_id>', methods=['DELETE'])
def delete_volunt(volunteer_id):
    volunteer = get_volunteer_info_by_id(volunteer_id)

    if volunteer:
        if delete_volunteer_info_by_id(volunteer_id):
            return jsonify({'msg': '删除成功'})

    return jsonify({'error': '未找到该义工信息'}), 404


@index_page.route('/volunteer_update/<int:volunteer_id>', methods=['POST'])
def update_volunteer(volunteer_id):
    data = request.get_json()
    volunteer = get_volunteer_info_by_id(volunteer_id)

    if volunteer:
        if update_volunteer_info_by_id(volunteer_id, data.get('volunteerName'), data.get('gender'), data.get('age'),
                                       data.get('phone'), data.get('id_card'), data.get('checkin_date'),
                                       data.get('checkout_date'),
                                       data.get('description'), data.get('imgset_dir'), data.get('profile_photo'),
                                       data.get('createby')
                                       ):
            return jsonify({'msg': '更新成功'})

    return jsonify({'error': '更新失败'}), 404


# 使用列表存储义工信息
volunteer_list = []


# 添加义工接口
@index_page.route('/volunteer/add-one', methods=['POST'])
def add_volunt():
    data = request.get_json()
    if add_volunteer_info(data.get('volunteerName'), data.get('age'), data.get('gender'),
                          data.get('id_card'), data.get('checkin_date'), data.get('checkout_date'),
                          data.get('phone'), data.get('description'), data.get('createby')
                          ) is not None:
        return {'status': 'success'}

    return {'status': 'error'}
