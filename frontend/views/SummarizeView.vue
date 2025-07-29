<!-- frontend/views/SummarizeView.vue -->
<template>
  <div class="p-6 max-w-2xl mx-auto">
    <h1 class="text-2xl font-bold mb-4">Daily Meeting Minutes Summarizer</h1>

    <textarea v-model="inputText" rows="8" class="w-full border rounded p-2 mb-4" placeholder="오늘 한 업무 내용을 입력하세요..." ></textarea>

    <button @click="summarize" class="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded mb-4">
      요약 요청
    </button>

    <div v-if="result">
      <h2 class="text-xl font-semibold mt-6">Summary</h2>
      <p class="mb-2">{{ result.summary }}</p>

      <h2 class="text-xl font-semibold mt-4">Tags</h2>
      <p class="mb-2">{{ result.tags.join(', ') }}</p>

      <h2 class="text-xl font-semibold mt-4">Feedback</h2>
      <p>{{ result.feedback }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const inputText = ref('')
const result = ref(null)

const summarize = async () => {
  try {
    const res = await axios.post('http://localhost:8000/api/summarize', {
      text: inputText.value
    })
    result.value = res.data
  } catch (err) {
    alert('요약 요청 중 오류가 발생했습니다.')
    console.error(err)
  }
}
</script>
