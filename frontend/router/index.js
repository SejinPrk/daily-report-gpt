// frontend/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import MeetingResultView from "../views/MeetingResultView.vue";
import MeetingForm from "../views/MeetingForm.vue";

const routes = [
  {
    path: '/',
    name: 'MeetingForm',
    component: MeetingForm
  },
  {
    path: '/result',
    name: 'MeetingResult',
    component: MeetingResultView
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
