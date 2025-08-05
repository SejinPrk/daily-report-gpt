<!-- frontend/components/GlobalLoading.vue -->
<template>
  <div
    v-if="loadingStore.isLoading('global')"
    class="fixed inset-0 bg-black bg-opacity-40 z-[9999] flex items-center justify-center"
  >
    <div class="bg-white rounded-xl shadow-xl p-6 flex flex-col items-center animate-fade-in">
      <svg
        class="w-10 h-10 text-blue-500 animate-spin mb-3"
        fill="none"
        viewBox="0 0 24 24"
      >
        <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
        <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z" />
      </svg>
      <p class="text-gray-800 text-lg font-medium">잠시만 기다려 주세요...</p>
    </div>
  </div>
</template>

<script setup>
import { useLoadingStore } from '@/stores/useLoadingStore'
const loadingStore = useLoadingStore()
</script>
