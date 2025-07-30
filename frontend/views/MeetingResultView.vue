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

    <!-- 2. 태그 -->
    <section>
      <h2 class="text-xl font-semibold mb-2">🏷️ 태그</h2>
      <p class="mb-4">{{ summaryData.tags.join(', ') }}</p>
    </section>

    <!-- 3. 피드백 -->
    <section>
      <h2 class="text-xl font-semibold mb-2">🗣️ 피드백</h2>
      <p class="mb-4">{{ summaryData.feedback }}</p>
    </section>
  </div>
</template>

<script setup>
import {ref, watch} from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const result = ref({})
const summaryData = ref({
  summary: '',
  tags: [],
  feedback: ''
})

watch(
  () => route.query,
  async (query) => {
    if (!query.raw_text) return  // 최소 조건 체크
    try {
      const res1 = await axios.post('/api/minutes', query)
      result.value = res1.data

      const res2 = await axios.post('/api/summarize', {
        text: res1.data.minutes
      })
      summaryData.value = res2.data
    } catch (err) {
      console.error('요약 또는 회의록 생성 오류:', err)
    }
  },
  { immediate: true }
)
</script>
