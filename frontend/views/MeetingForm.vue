<template>
  <div class="p-6 max-w-2xl mx-auto">
    <h1 class="text-2xl font-bold mb-4">회의 정보 입력</h1>

    <div class="grid gap-4">
      <input v-model="form.date" type="date" class="input" placeholder="회의 날짜" />
      <input v-model="form.author" class="input" placeholder="작성자" />
      <input v-model="form.participants" class="input" placeholder="참석자 (쉼표로 구분)" />
      <input v-model="form.location" class="input" placeholder="회의 장소" />
      <input v-model="form.time_range" class="input" placeholder="시간 (예: 09:30 ~ 10:30)" />
      <textarea v-model="form.raw_text" rows="6" class="textarea" placeholder="회의 메모 내용을 자유롭게 입력하세요"></textarea>

      <button @click="goToResult" class="btn">요약 생성</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const form = ref({
  date: '',
  author: '',
  participants: '',
  location: '',
  time_range: '',
  raw_text: ''
})

const goToResult = () => {
  router.push({ name: 'MeetingResult', query: form.value })
}
</script>

<style scoped>
.input, .textarea {
  border: 1px solid #ccc;
  border-radius: 6px;
  padding: 0.5rem;
  width: 100%;
}
.btn {
  padding: 0.5rem 1rem;
  background-color: #2563eb;
  color: white;
  border-radius: 6px;
  border: none;
}
</style>
