<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900 flex items-center justify-center p-4">
    <div class="w-full max-w-md">
      <!-- Logo/Header Section -->
      <div class="text-center mb-8">
        <div class="inline-flex items-center justify-center w-16 h-16 bg-gradient-to-br from-purple-600 to-indigo-600 rounded-2xl shadow-lg mb-4">
          <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 4v16M17 4v16M3 8h4m10 0h4M3 12h18M3 16h4m10 0h4M4 20h16a1 1 0 001-1V5a1 1 0 00-1-1H4a1 1 0 00-1 1v14a1 1 0 001 1z"/>
          </svg>
        </div>
        <h1 class="text-3xl font-light text-white mb-2">Create Account</h1>
        <p class="text-gray-400 text-sm">Join Movie Bank and start your cinematic journey</p>
      </div>

      <!-- Register Card -->
      <div class="bg-gray-800 rounded-2xl shadow-xl p-8 backdrop-blur-sm bg-opacity-95 border border-gray-700">
        <form class="space-y-6" @submit.prevent="handleRegister">
          <!-- Name Field -->
          <div>
            <label class="block text-sm font-medium text-gray-300 mb-2">
              Full Name
            </label>
            <div class="relative">
              <input
                type="text"
                v-model="name"
                required
                class="w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent transition-all duration-200 placeholder-gray-400 text-white"
                placeholder="Enter your full name"
              />
              <div class="absolute inset-y-0 right-0 flex items-center pr-3">
                <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"/>
                </svg>
              </div>
            </div>
          </div>

          <!-- Email Field -->
          <div>
            <label class="block text-sm font-medium text-gray-300 mb-2">
              Email Address
            </label>
            <div class="relative">
              <input
                type="email"
                v-model="email"
                required
                class="w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent transition-all duration-200 placeholder-gray-400 text-white"
                placeholder="your.email@example.com"
              />
              <div class="absolute inset-y-0 right-0 flex items-center pr-3">
                <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 12a4 4 0 10-8 0 4 4 0 008 0zm0 0v1.5a2.5 2.5 0 005 0V12a9 9 0 10-9 9m4.5-1.206a8.959 8.959 0 01-4.5 1.207"/>
                </svg>
              </div>
            </div>
          </div>

          <!-- Password Field -->
          <div>
            <label class="block text-sm font-medium text-gray-300 mb-2">
              Password
            </label>
            <div class="relative">
              <input
                type="password"
                v-model="password"
                required
                class="w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent transition-all duration-200 placeholder-gray-400 text-white"
                placeholder="Create a password"
              />
              <div class="absolute inset-y-0 right-0 flex items-center pr-3">
                <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>
                </svg>
              </div>
            </div>
          </div>

          <!-- Confirm Password Field -->
          <div>
            <label class="block text-sm font-medium text-gray-300 mb-2">
              Confirm Password
            </label>
            <div class="relative">
              <input
                type="password"
                v-model="confirmPassword"
                required
                class="w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent transition-all duration-200 placeholder-gray-400 text-white"
                placeholder="Confirm your password"
              />
              <div class="absolute inset-y-0 right-0 flex items-center pr-3">
                <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/>
                </svg>
              </div>
            </div>
          </div>

          <!-- Password Requirements -->
          <div class="p-3 bg-gray-700 rounded-lg">
            <p class="text-xs text-gray-400 mb-2">Password must:</p>
            <ul class="text-xs text-gray-400 space-y-1">
              <li class="flex items-center" :class="{'text-green-400': password.length >= 6}">
                <svg class="w-3 h-3 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path v-if="password.length >= 6" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                  <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                </svg>
                Be at least 6 characters
              </li>
              <li class="flex items-center" :class="{'text-green-400': password === confirmPassword && confirmPassword.length > 0}">
                <svg class="w-3 h-3 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path v-if="password === confirmPassword && confirmPassword.length > 0" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                  <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                </svg>
                Passwords must match
              </li>
            </ul>
          </div>

          <!-- Submit Button -->
          <div>
            <button
              type="submit"
              :disabled="loading || password !== confirmPassword || password.length < 6"
              class="w-full bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-700 hover:to-indigo-700 disabled:from-gray-600 disabled:to-gray-700 text-white py-3 px-4 rounded-lg font-medium transition-all duration-200 transform hover:scale-[1.02] disabled:scale-100 focus:ring-2 focus:ring-purple-500 focus:ring-offset-2 focus:ring-offset-gray-800"
            >
              <span class="flex items-center justify-center">
                <svg v-if="loading" class="animate-spin -ml-1 mr-2 h-4 w-4 text-white" fill="none" viewBox="0 0 24 24">
                  <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"/>
                  <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"/>
                </svg>
                {{ loading ? 'Creating account...' : 'Create Account' }}
              </span>
            </button>
          </div>

          <!-- Divider -->
          <div class="relative">
            <div class="absolute inset-0 flex items-center">
              <div class="w-full border-t border-gray-600"></div>
            </div>
            <div class="relative flex justify-center text-sm">
              <span class="px-2 bg-gray-800 text-gray-400">Already have an account?</span>
            </div>
          </div>

          <!-- Login Link -->
          <div class="text-center">
            <button
              type="button"
              @click="switchToLogin"
              class="text-purple-400 hover:text-purple-300 font-medium transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:ring-offset-2 focus:ring-offset-gray-800 rounded-lg px-3 py-2"
            >
              Sign in to your account
            </button>
          </div>
        </form>

        <!-- Error Message -->
        <div v-if="error" class="mt-6 p-4 bg-red-900/50 border border-red-700 rounded-lg">
          <div class="flex items-center">
            <svg class="w-5 h-5 text-red-400 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
            <span class="text-red-300 text-sm">{{ error }}</span>
          </div>
        </div>

        <!-- API Response (for debugging) -->
        <div v-if="apiResponse" class="mt-6 p-4 bg-gray-700 rounded-lg">
          <h3 class="text-sm font-medium text-gray-300 mb-2">API Response:</h3>
          <pre class="text-xs text-gray-400 overflow-auto max-h-32">{{ apiResponse }}</pre>
        </div>
      </div>

      <!-- Footer -->
      <div class="text-center mt-8">
        <p class="text-gray-500 text-xs">
          © 2024 Movie Bank. Curate your cinematic experience.
        </p>
      </div>
    </div>
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

<style scoped>
/* Smooth transitions for all interactive elements */
input, button {
  transition: all 0.2s ease-in-out;
}

/* Custom focus styles for dark theme */
input:focus {
  box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.3);
}

/* Loading animation */
@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

.animate-spin {
  animation: spin 1s linear infinite;
}
</style>