<!-- src/views/LoginView.vue -->
<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="handleLogin">
      <div>
        <label>Email:</label>
        <input type="email" v-model="email" required>
      </div>
      <div>
        <label>Password:</label>
        <input type="password" v-model="password" required>
      </div>
      <button type="submit" :disabled="loading">
        {{ loading ? 'Logging in...' : 'Login' }}
      </button>
    </form>
    <div v-if="error" style="color: red; margin-top: 10px;">
      {{ error }}
    </div>
    <div v-if="apiResponse" style="margin-top: 10px;">
      <h3>API Response:</h3>
      <pre>{{ apiResponse }}</pre>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { movieService } from '@/services/movieService'

const email = ref('')
const password = ref('')
const loading = ref(false)
const error = ref('')
const apiResponse = ref<any>(null)
const router = useRouter()

const handleLogin = async () => {
  loading.value = true
  error.value = ''
  apiResponse.value = null

  try {
    const response = await movieService.login({
      email: email.value,
      password: password.value
    })

    localStorage.setItem('auth_token', response.data.access_token)
    apiResponse.value = response.data

    // Redirect to home
    router.push('/')

  } catch (err: any) {
    error.value = err.response?.data?.detail || 'Login failed'
    apiResponse.value = err.response?.data
  } finally {
    loading.value = false
  }
}
</script>