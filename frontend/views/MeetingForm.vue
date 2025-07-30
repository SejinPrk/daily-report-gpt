<template>
  <div class="p-6 max-w-2xl mx-auto">
    <h1 class="text-2xl font-bold mb-4">회의 정보 입력</h1>

    <!-- 날짜 -->
    <div class="w-1/2 max-w-[250px]">
      <label class="block text-sm font-medium mb-1">날짜</label>
      <input
        v-model="form.date"
        type="date"
        class="w-full border border-gray-300 rounded px-3 py-2"
      />
    </div>

    <!-- 작성자 -->
    <div class="w-1/2 max-w-[250px]">
      <label class="block text-sm font-medium mb-1">작성자</label>
      <input
        v-model="form.author"
        class="w-full border border-gray-300 rounded px-3 py-2"
        placeholder="작성자"
      />
    </div>

    <!-- 장소 -->
    <div class="w-1/2 max-w-[250px]">
      <label class="block text-sm font-medium mb-1">회의 장소</label>
      <input v-model="form.location" class="input w-full" placeholder="예: 본사 A회의실" />
    </div>

    <!-- 시간 선택 -->
    <div class="w-1/2 max-w-[250px]">
      <label class="block text-sm font-medium mb-1">시간</label>
      <div class="flex gap-2 items-center w-full">
        <select v-model="startTime" class="w-1/2 border border-gray-300 rounded px-2 py-1">
          <option v-for="t in timeOptions" :key="t" :value="t">{{ t }}</option>
        </select>
        <span>~</span>
        <select v-model="endTime" class="w-1/2 border border-gray-300 rounded px-2 py-1">
          <option v-for="t in timeOptions" :key="t" :value="t">{{ t }}</option>
        </select>
      </div>
    </div>

    <!-- 참석자 -->
    <div class="mb-4 max-w-[600px]">
      <label class="block text-sm font-medium mb-1">참석자</label>
      <input v-model="form.participants" class="w-full border border-gray-300 rounded px-3 py-2" placeholder="참석자 (쉼표로 구분)" />
    </div>

    <!-- 내용 -->
    <div class="mb-4">
      <label class="block text-sm font-medium mb-1">회의 내용</label>
      <div class="w-full">
        <textarea v-model="form.raw_text" rows="6" class="w-full border border-gray-300 rounded px-3 py-2" placeholder="회의 내용을 입력하세요"></textarea>
      </div>
    </div>

    <button @click="goToResult" class="btn">회의록 생성</button>
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

const startTime = ref('09:00')
const endTime = ref('10:00')

// 30분 단위로 회의실 예약
const timeOptions = Array.from({ length: 24 }, (_, i) => {
  const hour = 8 + Math.floor(i / 2)
  const min = i % 2 === 0 ? '00' : '30'
  return `${String(hour).padStart(2, '0')}:${min}`
})

const goToResult = () => {
  form.value.time_range = `${startTime.value} ~ ${endTime.value}`
  router.push({ name: 'MeetingResult', query: form.value })
}
</script>

<style scoped>
.btn {
  padding: 0.5rem 1rem;
  background-color: #2563eb;
  color: white;
  border-radius: 6px;
  border: none;
}
</style>
