<!-- src/views/HomeView.vue -->
<template>
  <div>
    <h1>Welcome to Movie Bank</h1>
    <p>You are logged in successfully!</p>
    
    <!-- Search Bar -->
    <div>
      <h2>Search Movies</h2>
      <form @submit.prevent="handleSearch">
        <input 
          type="text" 
          v-model="searchQuery" 
          placeholder="Search for movies..."
          :disabled="searchLoading"
        />
        <button type="submit" :disabled="searchLoading || !searchQuery">
          {{ searchLoading ? 'Searching...' : 'Search' }}
        </button>
      </form>
    </div>

    <!-- Search Results -->
    <div v-if="searchResults">
      <h3>Search Results ({{ searchResults.total_count }} found):</h3>
      <div v-if="searchResults.results.length === 0">
        <p>No movies found. Try a different search term.</p>
      </div>
      <div v-else>
        <button @click="logResultsToConsole">Log Results to Console</button>
        <pre>{{ searchResults }}</pre>
      </div>
    </div>

    <!-- User Profile -->
    <div v-if="userProfile">
      <h2>User Profile:</h2>
      <pre>{{ userProfile }}</pre>
    </div>

    <button @click="handleLogout">Logout</button>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { movieService } from '@/services/movieService'
import type { SearchResponse } from '@/types/movies'

const userProfile = ref<any>(null)
const searchQuery = ref('')
const searchResults = ref<SearchResponse | null>(null)
const searchLoading = ref(false)
const router = useRouter()

onMounted(async () => {
  try {
    const response = await movieService.getProfile()
    userProfile.value = response.data
  } catch (error) {
    console.error('Failed to fetch profile:', error)
  }
})

const handleSearch = async () => {
  if (!searchQuery.value.trim()) return

  searchLoading.value = true
  searchResults.value = null

  try {
    const response = await movieService.searchMovies(searchQuery.value)
    searchResults.value = response.data
    console.log('Search results:', response.data)
  } catch (error) {
    console.error('Search failed:', error)
    alert('Search failed. Please try again.')
  } finally {
    searchLoading.value = false
  }
}

const logResultsToConsole = () => {
  if (searchResults.value) {
    console.log('Full search results:', searchResults.value)
    searchResults.value.results.forEach((movie, index) => {
      console.log(`Movie ${index + 1}:`, movie)
    })
  }
}

const handleLogout = () => {
  localStorage.removeItem('auth_token')
  router.push('/login')
}
</script>