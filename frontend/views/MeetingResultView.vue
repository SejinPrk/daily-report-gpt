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
      <button @click="isEditOpen = true" class="text-sm text-blue-600 hover:underline">
          ✏️ 수정
        </button>
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

    <!-- 회의록 수정 팝업 -->
    <div v-if="isEditOpen" class="fixed inset-0 bg-black bg-opacity-40 flex items-center justify-center z-50">
      <div class="bg-white rounded-lg shadow-xl w-full max-w-2xl p-6">
        <h3 class="text-lg font-semibold mb-4">📝 회의록 수정</h3>
        <textarea
          v-model="editedMinutes"
          rows="10"
          class="w-full border border-gray-300 rounded p-3 mb-4"
        ></textarea>

        <div class="flex justify-end space-x-2">
          <button @click="isEditOpen = false" class="px-4 py-2 rounded border">취소</button>
          <button @click="saveEditedMinutes" class="px-4 py-2 bg-blue-600 text-white rounded">
            저장
          </button>
        </div>
      </div>
    </div>

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

// 팝업 관련 상태
const isEditOpen = ref(false)
const editedMinutes = ref('')


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

async function saveEditedMinutes() {
  try {
    loading.show()

    const payload = {
      minutes: editedMinutes.value
    }

    await axios.post('/api/save-edited-minutes', payload)

    result.value.minutes = editedMinutes.value
    isEditOpen.value = false
    alert('수정된 회의록이 저장되었습니다.')
  } catch (e) {
    console.error('저장 오류:', e)
    alert('저장에 실패했습니다.')
  } finally {
    loading.hide()
  }
}
</script>
