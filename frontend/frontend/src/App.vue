<!-- src/App.vue -->
<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

onMounted(() => {
  const token = localStorage.getItem('auth_token')
  if (!token && router.currentRoute.value.path !== '/login') {
    router.push('/login')
  }
})
</script>