import {request} from "./request";
import axios from 'axios';
// import {request2} from "./request";

//用户登录请求
export function login_user(user) {
    console.log('login_user')
    console.log(JSON.stringify(user))
    return request({
        url: '/admin/login/',
        method: 'post',
        data: JSON.stringify(user),
        headers: {
            'Content-Type': 'application/json',
          },
    })
}

//用户注册请求
export function register_user(registerData) {
    console.log('register')
    return request({
        url: '/admin/register/',
        method: 'post',
        data: registerData,
        headers: {
            'Content-Type': 'application/json',
        },
    })
}

//用户注册请求
export function search_old(searchData) {
    console.log('search_old')
    return axios({
        url: 'http://127.0.0.1:5000/elderly',
        method: 'get',
        data: searchData,
        headers: {
            'Content-Type': 'application/json',
        },
    })
}