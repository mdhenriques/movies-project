<!-- src/views/HomeView.vue -->
<template>
  <div>
    <h1>Welcome to Movie Bank</h1>
    <p>You are logged in successfully!</p>
    <button @click="handleLogout">Logout</button>
    
    <div v-if="userProfile">
      <h2>User Profile:</h2>
      <pre>{{ userProfile }}</pre>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { movieService } from '@/services/movieService'

const userProfile = ref<any>(null)
const router = useRouter()

onMounted(async () => {
  try {
    const response = await movieService.getProfile()
    userProfile.value = response.data
  } catch (error) {
    console.error('Failed to fetch profile:', error)
  }
})

const handleLogout = () => {
  localStorage.removeItem('auth_token')
  router.push('/login')
}
</script>