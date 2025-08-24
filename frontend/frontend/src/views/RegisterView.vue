<!-- src/views/RegisterView.vue -->
<template>
  <div>
    <h1>Create Account</h1>
    <form @submit.prevent="handleRegister">
      <div>
        <label>Name:</label>
        <input type="text" v-model="name" required>
      </div>
      <div>
        <label>Email:</label>
        <input type="email" v-model="email" required>
      </div>
      <div>
        <label>Password:</label>
        <input type="password" v-model="password" required>
      </div>
      <div>
        <label>Confirm Password:</label>
        <input type="password" v-model="confirmPassword" required>
      </div>
      <button type="submit" :disabled="loading">
        {{ loading ? 'Creating account...' : 'Register' }}
      </button>
    </form>
    
    <div v-if="error" style="color: red; margin-top: 10px;">
      {{ error }}
    </div>
    
    <div v-if="apiResponse" style="margin-top: 10px;">
      <h3>API Response:</h3>
      <pre>{{ apiResponse }}</pre>
    </div>

    <p style="margin-top: 20px;">
      Already have an account? 
      <a href="#" @click.prevent="switchToLogin">Login here</a>
    </p>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { movieService } from '@/services/movieService'

const name = ref('')
const email = ref('')
const password = ref('')
const confirmPassword = ref('')
const loading = ref(false)
const error = ref('')
const apiResponse = ref<any>(null)
const router = useRouter()

const handleRegister = async () => {
  // Basic validation
  if (password.value !== confirmPassword.value) {
    error.value = 'Passwords do not match'
    return
  }

  if (password.value.length < 6) {
    error.value = 'Password must be at least 6 characters'
    return
  }

  loading.value = true
  error.value = ''
  apiResponse.value = null

  try {
    const response = await movieService.register({
      name: name.value,
      email: email.value,
      password: password.value
    })

    // Store the token
    localStorage.setItem('auth_token', response.data.access_token)
    apiResponse.value = response.data

    // Redirect to home after successful registration
    setTimeout(() => {
      router.push('/')
    }, 1000)

  } catch (err: any) {
    error.value = err.response?.data?.detail || 'Registration failed. Please try again.'
    apiResponse.value = err.response?.data
  } finally {
    loading.value = false
  }
}

const switchToLogin = () => {
  router.push('/login')
}
</script>