// frontend/vite.config.mjs

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path'

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname)
    }
  },
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000', // FastAPI 서버 주소
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '/api') // 그대로 유지 (prefix="/api")
      }
    }
  }
})
