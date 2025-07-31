<!-- frontend/App.vue -->
<template>
  <div class="relative min-h-screen bg-gray-50 text-gray-800">
    <router-view />
    <GlobalLoading />
  </div>
</template>

<script setup>
import GlobalLoading from "@/components/GlobalLoading.vue";
</script>

<style>
/* Tailwind 사용 시, 글로벌 스타일 최소화 */
</style>

