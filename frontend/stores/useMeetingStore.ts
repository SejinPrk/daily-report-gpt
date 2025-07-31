// stores/useMeetingStore.ts
import { defineStore } from 'pinia'
import { ref } from 'vue'

interface MeetingForm {
  date: string
  author: string
  participants: string
  location: string
  time_range: string
  raw_text: string
}

export const useMeetingStore = defineStore('meeting', () => {
  const formData = ref<MeetingForm | null>(null)

  function setFormData(data: MeetingForm) {
    formData.value = data
  }

  return { formData, setFormData }
})
