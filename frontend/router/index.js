// frontend/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import SummarizeView from '../views/SummarizeView.vue'

const routes = [
  {
    path: '/',
    name: 'Summarize',
    component: SummarizeView
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
