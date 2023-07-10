<template>
    <div style="display: flex;flex-direction: row;justify-content: space-around;width:100%;height:100%;">
        <div style="height: 500px;width:900px;border: 2px dotted;">
            <!-- <video id="myFlvVideo" muted autoplay width="500px" height="250px" /> -->
            <!-- <video controls="controls" class="demo-video" ref="player" muted  @dblclick="fullScreen"></video> -->
            <img v-show="faceVisible" style="display: block;-webkit-user-select: none;margin: auto;" src="http://127.0.0.1:5000/cam/video_feed"
                height="500" width="900">
                <img v-show="fallVisible" style="display: block;-webkit-user-select: none;margin: auto;" src="http://127.0.0.1:5000/cam/video_feed_2"
                height="500" width="900">
                <button class="changeBtn" @click="changeCamera">切换摄像头</button>
        </div>
        <el-card style="width:300px;height:500px;">


        </el-card>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return {
            faceVisible:true,
            fallVisible:false,
        }
    },
    methods:{
        changeCamera(){
            this.faceVisible = !this.faceVisible;
            this.fallVisible = !this.fallVisible;
        }
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
 width:200px;
 height: 40px;
}

.changeBtn:hover, button:active {
 -webkit-transform: translate(0px,5px);
 -ms-transform: translate(0px,5px);
 transform: translate(0px,5px);
 border-bottom: 1px solid #2ecc71;
}
</style>