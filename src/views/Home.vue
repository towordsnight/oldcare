<template>
    <div style="background-color: rgb(139, 183, 168);height:50px;width:100%;display: flex;flex-direction: row;">
        <el-button type="text" @click="toggle" style="margin-top: 17px;margin-left:20px;">
            <el-icon :size="25">
                <svg t="1688450180361" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                    p-id="14707" width="128" height="128">
                    <path
                        d="M130.901333 529.493333l149.205334 130.517334a8.533333 8.533333 0 0 0 14.122666-6.4V392.533333a8.533333 8.533333 0 0 0-14.122666-6.4L130.901333 
                        516.608a8.533333 8.533333 0 0 0 0 12.8z"
                        fill="#515151" p-id="14708"></path>
                    <path
                        d="M128 213.333333m42.666667 0l682.666666 0q42.666667 0 42.666667 42.666667l0 0q0 42.666667-42.666667 42.666667l-682.666666 
                        0q-42.666667 0-42.666667-42.666667l0 0q0-42.666667 42.666667-42.666667Z"
                        fill="#515151" p-id="14709"></path>
                    <path
                        d="M128 725.333333m42.666667 0l682.666666 0q42.666667 0 42.666667 42.666667l0 0q0 42.666667-42.666667 42.666667l-682.666666 
                        0q-42.666667 0-42.666667-42.666667l0 0q0-42.666667 42.666667-42.666667Z"
                        fill="#515151" p-id="14710"></path>
                    <path
                        d="M384 469.333333m42.666667 0l426.666666 0q42.666667 0 42.666667 42.666667l0 0q0 42.666667-42.666667 42.666667l-426.666666 
                        0q-42.666667 0-42.666667-42.666667l0 0q0-42.666667 42.666667-42.666667Z"
                        fill="#515151" p-id="14711"></path>
                </svg>
            </el-icon>
        </el-button>
        <div style="display: block;margin: 0 auto;">
            <span style="font-size: 40px;">
                智 能 看 护 系 统
            </span>

        </div>
    </div>
    <div class="common-layout">

        <el-container class="container">
            <el-aside class="aside" :style="{ 'width': (isCollapse ? '63px' : '230px') }">
                <Menu :isCollapse="isCollapse" />

            </el-aside>
            <el-container>
                <el-main class="main">
                    <img v-show="false" style="display: block;-webkit-user-select: none;margin: auto;" src="http://127.0.0.1:5000/cam/video_feed"
                height="500" width="900">
                <img v-show="false" style="display: block;-webkit-user-select: none;margin: auto;" src="http://127.0.0.1:5000/cam/video_feed_2"
                height="500" width="900">
                    <router-view />

                </el-main>
            </el-container>
        </el-container>
    </div>
</template>
<script lang="ts" setup>
import Menu from './Menu.vue';
import { ref } from 'vue'
import { Fold } from '@element-plus/icons-vue';
let isCollapse = ref(false)
const toggle = (): void => {
    isCollapse.value = !isCollapse.value
}
</script>

<style scoped lang="scss">
.container {
    height: 90vh;

    .aside {
        overflow: hidden;
    }

    .header {
        background: #f3ebf5;
        height: 80px;
    }

    .common-layout {
        background: #accebc;
    }
}

.svg_con {
    height: auto;

}</style>