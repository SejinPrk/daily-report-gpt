<!--frontend/view/MeetingResultView.vue-->
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
import {ref, watchEffect} from 'vue'
import { useRouter, useRoute } from 'vue-router'
import axios from 'axios'
import { useLoadingStore } from '@/stores/useLoadingStore'
import {useMeetingStore} from "@/stores/useMeetingStore";

const router = useRouter()
const route = useRoute()
const meetingStore = useMeetingStore()

const result = ref({})
const loading = useLoadingStore() // 전역 로딩창
const summaryData = ref({
  summary: '',
  tags: [],
  feedback: ''
})

watchEffect(async () => {
  const formData = meetingStore.formData

  if (!formData || !formData.raw_text) {
    alert('회의 정보가 없습니다. 처음 화면으로 돌아갑니다.')
    await router.push({name: 'MeetingForm'})
    return
  }

  try {
    loading.show()

    const res1 = await axios.post('/api/minutes', formData)
    result.value = res1.data

    const res2 = await axios.post('/api/summarize', { text: res1.data.minutes })
    summaryData.value.summary = res2.data.summary
    summaryData.value.tags = res2.data.tags

    const res3 = await axios.post('/api/feedback', { meeting_minutes: res1.data.minutes })
    summaryData.value.feedback = res3.data.feedback
  } catch (e) {
    console.error('요약 오류:', e)
  } finally {
    loading.hide()
  }
})
</script>
