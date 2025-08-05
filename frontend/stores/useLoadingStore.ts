// stores/loadingStore.ts

import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useLoadingStore = defineStore('loading', () => {
  const loadingMap = ref(new Map<string, boolean>())

  function show(id = 'global') {
    loadingMap.value.set(id, true)
  }

  function hide(id = 'global') {
    loadingMap.value.set(id, false)
  }

  function isLoading(id = 'global') {
    return loadingMap.value.get(id) || false
  }

  return { loadingMap, show, hide, isLoading }
})