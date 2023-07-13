<template>
    <div style="display: flex;flex-direction: row;justify-content: space-around;width:100%;height:100%;">
        <div style="height: 500px;width:800px;border: 2px dotted;">
            <!-- <img v-show="faceVisible" style="display: block;-webkit-user-select: none;margin: auto;"
                src="http://127.0.0.1:5001/video_feed" height="500" width="900">
            <img v-show="fallVisible" style="display: block;-webkit-user-select: none;margin: auto;"
                src="http://127.0.0.1:5001/video_feed_2" height="500" width="900"> -->
            <img v-show="faceVisible" style="display: block;margin: auto;" :src="faceCamera" height="500" width="800">
            <button class="changeBtn" @click="changeCamera">切换摄像头</button>
        </div>
        <el-card style="width:300px;height:500px;background-color: #fcfffc;border-radius: 50px;">
            <el-scrollbar height="450px" style="margin-top: 5px;">
                <div v-for="(item, index) in cardContent" :key="index"
                    style="margin-left: 5px;width:245px;height:80px;margin-top: 5px;">
                    <el-card style="background: #e7f2e9;width:245px;height:80px;border-radius: 30px;">
                        <span style="font-size: 20px;">{{ item.content }}</span>
                    </el-card>
                </div>
            </el-scrollbar>

        </el-card>

        <audio controls ref="audio" hidden>
            <source src="../assets/warning.mp3" />
        </audio>
    </div>
</template>

<script>
import axios from 'axios';
import io from 'socket.io-client';
import { Base64 } from 'js-base64';
export default {
    data() {
        return {
            faceVisible: true,
            localCamera: false,

            cardContent: [],
            faceCamera: null,
        }
    },
    beforeDestroy() { //订阅事件记得要取消---否则多次订阅会引发多次消息返回
        if (!this.$socket) return
        this.sockets.unsubscribe('msgContent')
        this.$socket.close()
    },
    created() {
        const script = document.createElement("script");
        script.type = "text/javascript";
        script.src = "https://cdn.bootcss.com/jquery/3.2.0/jquery.js";
        script.onerror = () => {
            throw new Error("无法加载");
        };
        document.body.appendChild(script);

        axios.get(`http://127.0.0.1:5001/video_remote`).then(res => {
            console.log(res)
            //页面刚进入时开启长连接
            this.socket = io.connect('ws://localhost:5001/echo', {
                timeout: 300000,
                reconnectionDelayMax: 1000,
                reconnectionDelay: 500
            })
            this.socket.on('connect', () => {
                console.log('建立链接')
                this.socket.emit('server_response', { 'data': 'I\'m connected!' })


            })
            this.socket.on('disconnect', () => {
                console.log('连接断开')
                this.socket.emit('server_response', { 'data': 'I\'m disconnected!' });
            })
            this.socket.on('server_response', (arg, callback) => {
                console.log(arg);
                this.cardContent.unshift({
                    content: arg
                });
            })
            this.socket.on('img', (arg, callback) => {
                // console.log(arg);
                const decoder = new TextDecoder('utf-8');
                const text = decoder.decode(arg);
                // this.faceCamera = Base64.decode(arg);
                this.faceCamera = 'data:image/jpg;base64,' + text;
            })
            this.socket.on('error message', msg => {
                console.log('error:' + msg)

            })

        }).catch(err => {
            console.log(err.response)
        })

    },

    methods: {
        changeCamera() {
            if (this.localCamera == false) {
                axios.get(`http://127.0.0.1:5001/video_locality`).then(res => {
                    console.log(res)
                    this.localCamera = true
                }).catch(err => {
                    console.log(err.response)
                })

            } else {
                axios.get(`http://127.0.0.1:5001/video_locality_close`).then(res => {
                    console.log(res)
                    this.localCamera = false
                }).catch(err => {
                    console.log(err.response)
                })

            }

            this.$refs.audio.currentTime = 0; //从头开始播放提示音
            this.$refs.audio.play(); //播放
        },

    }
}
</script>

<style>
.changeBtn {
    position: relative;
    padding: 10px 40px;
    margin: 10px 10px 10px 0px;
    float: left;
    border-radius: 3px;
    font-size: 20px;
    color: #FFF;
    text-decoration: none;
    background-color: #7aecaa;
    border: none;
    border-bottom: 5px solid #7aecaa;
    text-shadow: 0px -2px #7aecaa;
    -webkit-transition: all 0.1s;
    transition: all 0.1s;
    width: 200px;
    height: 40px;
}

.changeBtn:hover,
button:active {
    -webkit-transform: translate(0px, 5px);
    -ms-transform: translate(0px, 5px);
    transform: translate(0px, 5px);
    border-bottom: 1px solid #2ecc71;
}
</style>