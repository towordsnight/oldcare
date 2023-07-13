import { createApp } from 'vue'
import App from './App.vue'

import router from './router/index.js'

import ElementPlus from 'element-plus'

import '../node_modules/element-plus/dist/index.css'
// 导入所有的el-icon图标
import * as ElIconModules from '../node_modules/@element-plus/icons-vue'

import axios from 'axios'


const app = createApp(App)

app.use(router)

app.use(ElementPlus)

app.mount('#app')





//  统一注册el-icon图标
for (let iconName in ElIconModules) {
    app.component(iconName, ElIconModules[iconName])
}