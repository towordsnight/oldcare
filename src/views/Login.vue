<template>
    <div class="container" style="width:100%;height:100%;">
        <div class="login_main">
            <!-- 整个注册盒子 -->
            <div class="loginbox">
                <!-- 左侧的注册盒子 -->
                <div class="loginbox-in">
                    <div class="userbox">
                        <svg t="1680521604004" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                            width="25px" height="25px">
                            <path d="M725.333333 721.066667l-38.4-38.4H379.733333l-38.4 
                                    38.4V768h384v-46.933333z m85.333334-38.4v170.666666H256v-170.666666h4.266667l85.333333-85.333334h375.466667l89.6 
                                    85.333334z m-85.333334-320c0 106.666667-85.333333 192-192 192S341.333333 469.333333 341.333333 362.666667 426.666667 
                                    170.666667 533.333333 170.666667 725.333333 256 725.333333 362.666667z m-85.333333 0C640 302.933333 593.066667 256 
                                    533.333333 256S426.666667 302.933333 426.666667 362.666667s46.933333 106.666667 106.666666 106.666666S640 422.4 640 
                                    362.666667z" fill="#444444"></path>
                        </svg>
                        <input class="inp" id="user" v-model="user.username" placeholder="用户名">
                    </div>
                    <br>
                    <div class="pwdbox">
                        <svg t="1680522311002" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                            width="25px" height="25px">
                            <path
                                d="M418.133333 499.2c-21.333333-34.133333-29.866667-72.533333-29.866666-115.2 0-119.466667 93.866667-213.333333 
                                    213.333333-213.333333s213.333333 93.866667 213.333333 213.333333-93.866667 213.333333-213.333333 213.333333c-46.933333 
                                    0-85.333333-12.8-123.733333-38.4l-98.133334 98.133334 46.933334 46.933333-59.733334 59.733333-46.933333-46.933333-29.866667 
                                    29.866667 46.933334 46.933333L277.333333 853.333333 170.666667 746.666667l247.466666-247.466667zM601.6 256c-72.533333 0-128 
                                    55.466667-128 128s55.466667 128 128 128 128-55.466667 128-128-59.733333-128-128-128z"
                                fill="#444444"></path>
                        </svg>
                        <input class="inp" id="password" v-model="user.password" type="password" placeholder="密码">
                    </div>
                    <div>
                        <button class="login_btn" @click="login">登录</button>
                    </div>
                    <br>
                    <div style="margin-top: 53px;display: flex;">
                        <span style="font-size: 16px;margin-left: 50px;width: 80px;">没有账号？</span>
                        <button style="font-size: 16px;color: #4E655D;margin-left: 20px;width: 50px;" class="register_btn"
                            @click="register">注册</button>
                    </div>

                </div>

                <!-- 右侧的注册盒子 -->
                <div class="background">
                    <div class="title">智能看护系统</div>
                </div>

            </div>
        </div>
    </div>
</template>

<script >
import axios from 'axios';
export default {
    data() {
        return {
            user: {
                username: "",
                password: "",
            },
            user_admin: {
                name: "",
                password: "",
            }
        }
    },
    methods: {
        register() {
            this.$router.push('/register');
        },
        login() {
            this.$router.push('/home');
            if (this.user.username == "" || this.user.password == "") {
                this.$message({
                    showClose: true,
                    message: "用户名或密码为空",
                    type: 'error'
                })
            } else {
                // axios.post(`http://43.143.247.127:8088/user/login`,this.user)
                // .then(res => {
                //     console.log(res)
                //     if (res.data.code == 1 && res.data.data.permission == 1) {
                //         this.$router.push('/homepage');
                //         //弹出成功消息
                //         this.$message({
                //             showClose: true,
                //             message: '用户登录成功',
                //             type: 'success'
                //         })
                //         console.log(res)
                //         const token = res.data.data.token
                //         window.localStorage.clear('token');
                //         window.localStorage.setItem('token', token);
                //     }else if (res.data.code == 1 && res.data.data.permission == 2){
                //         //弹出消息
                //         this.$message({
                //             showClose: true,
                //             message: '您输入的账号密码为管理员身份，请选择管理员登录按钮',
                //             type: 'error'
                //         })
                //     } else if (res.data.code == 401){
                //         this.$message({
                //             showClose: true,
                //             message: "用户名或密码错误",
                //             type: 'error'
                //         })
                //     }
                //     });
            }

        },
    }
}


</script>

<style>
.login_main {
    width: 100%;
    height: 700px;
    background-image: url('../img/background2.jpg');
    background-size: cover;
}

.background{
    background-image: url('../img/background.jpg');
    background-size: cover;
}

.loginbox {
    display: flex;
    position: absolute;
    width: 800px;
    height: 400px;
    top: 40%;
    left: 50%;
    transform: translate(-50%, -50%);
    box-shadow: 0 12px 16px 0 rgba(0, 0, 0, 0.24), 0 17px 50px 0 #4E655D;
    box-shadow: 0 5px 16px 5px rgb(0, 0, 0);
}

.loginbox-in {
    background-color: #89AB9E;
    background-color: #acd5c4;
    background-color: #bfe5d5;
    width: 250px;
}

.userbox {
    margin-top: 120px;
    height: 30px;
    width: 230px;
    display: flex;
    margin-left: 25px;
}

.pwdbox {
    height: 30px;
    width: 225px;
    display: flex;
    margin-left: 25px;
}

.background {
    width: 570px;
    /* background-image: url('../img/background3.png');
    background-size: cover; */
    font-family: sans-serif;
}

.title {
    margin-top: 320px;
    margin-left: 40px;
    font-weight: bold;
    font-size: 30px;
    /*color: #6cddb4; */
    color: #000000;

}

.title:hover {
    font-size: 31px;
    transition: all 0.4s ease-in-out;
    cursor: pointer;
}

.uesr-text {
    position: left;
}

.inp {
    outline-style: none;
    border: 0;
    border-bottom: 1px solid #4f8889;
    background-color: transparent;
    height: 20px;
    font-family: sans-serif;
    font-size: 15px;
    color: #445b53;
    font-weight: bold;
}

.inp:focus {
    border-bottom: 2px solid #445b53;
    background-color: transparent;
    transition: all 0.2s ease-in;
    font-family: sans-serif;
    font-size: 15px;
    color: #445b53;
    font-weight: bold;

}

.inp:hover {
    border-bottom: 2px solid #445b53;
    background-color: transparent;
    transition: all 0.2s ease-in;
    font-family: sans-serif;
    font-size: 15px;
    color: #445b53;
    font-weight: bold;

}

.inp:-webkit-autofill {
    /* 修改默认背景框的颜色 */
    box-shadow: 0 0 0px 1000px #89AB9E inset !important;
    /* 修改默认字体的颜色 */
    -webkit-text-fill-color: #445b53;
}

.inp:-webkit-autofill::first-line {
    /* 修改默认字体的大小 */
    font-size: 15px;
    /* 修改默认字体的样式 */
    font-weight: bold;
}

.log-box {
    font-size: 12px;
    display: flex;
    justify-content: space-between;
    width: 190px;
    margin-left: 30px;
    color: #4E655D;
    margin-top: -5px;
    align-items: center;

}

.log-box-text {
    color: #4E655D;
    font-size: 12px;
    text-decoration: underline;
}

.login_btn {
    background-color: #5f8276;
    /* Green */
    border: none;
    color: #FAFAFA;
    padding: 5px 22px;
    text-align: center;
    text-decoration: none;
    font-size: 16px;
    border-radius: 20px;
    outline: none;
    margin-left: 50px;
    width: 150px;
    height: 30px;
}

.login_btn:hover {
    box-shadow: 0 16px 18px 0 rgba(0, 0, 0, 0.24), 0 17px 50px 0 rgba(0, 0, 0, 0.19);
    cursor: pointer;
    background-color: #0b5137;
    transition: all 0.2s ease-in;
}

.warn {
    margin-top: 60px;
    /* margin-right:120px; */
    margin-left: -120px;
    margin-bottom: 5px;
    font-weight: bold;
    font-size: 17px;
}

.register_btn {
    background-color: transparent;
    /* Green */
    border: none;
    text-decoration: none;
    font-size: 12px;
    /* border-radius: 20px;   */
    color: #4E655D;
    font-size: 12px;
    text-decoration: underline;
    display: flex;
    margin-left: 25px;
    outline: none;

}

.register_btn:hover {
    font-weight: bold;
    cursor: pointer;
}
</style> 