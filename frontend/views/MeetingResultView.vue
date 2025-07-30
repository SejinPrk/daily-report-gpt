<template>
  <div class="p-6 max-w-3xl mx-auto">
    <h1 class="text-2xl font-bold mb-6">📋 회의 리포트</h1>

    <!-- 1. 회의록 (LangChain 응답) -->
    <section>
      <h2 class="text-xl font-semibold mb-2">📝 회의록</h2>
      <pre class="whitespace-pre-wrap bg-gray-100 p-4 rounded mb-6">
        {{ result.minutes }}
      </pre>
    </section>

    <!-- 2. 요약 -->
    <section>
      <h2 class="text-xl font-semibold mb-2">📌 요약</h2>
      <p class="mb-4">{{ summaryData.summary }}</p>
    </section>

    <!-- 3. 태그 -->
    <section>
      <h2 class="text-xl font-semibold mb-2">🏷️ 태그</h2>
      <p class="mb-4">{{ summaryData.tags.join(', ') }}</p>
    </section>

    <!-- 4. 피드백 -->
    <section>
      <h2 class="text-xl font-semibold mb-2">🗣️ 피드백</h2>
      <p class="mb-4">{{ summaryData.feedback }}</p>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const result = ref({})
const summaryData = ref({
  summary: '',
  tags: [],
  feedback: ''
})

onMounted(async () => {
  try {
    // 1. 회의록 생성
    const res1 = await axios.post('/api/minutes', route.query)
    result.value = res1.data

    // 2. 추가 요약 분석 (SummarizeView 기능 활용)
    const res2 = await axios.post('/api/summarize', {
      text: res1.data.minutes
    })
    summaryData.value = res2.data
  } catch (err) {
    console.error('요약 또는 회의록 생성 오류:', err)
  }
})
</script>
