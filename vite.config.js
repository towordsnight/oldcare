import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

//https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('\src', import.meta.url))
    }
  },
  server: {
    host: 'localhost',
    port: 5174,
    proxy: {
      '/api': {
        target: 'http://8.130.83.55:3306',
        // secure: false, //如果是https接口，如要配置此参数
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''),
      },
      // '/navy': { // 设置第二个代理
      //   target: "http://43.143.247.127:9000",
      //   changeOrigin: true,
      //   rewrite: (path) => path.replace(/^\/navy/, ''),
      // },
    },
  },
})


