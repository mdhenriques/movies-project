<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900 flex">
    <!-- Sidebar -->
    <div 
      class="bg-gray-800 border-r border-gray-700 p-6 flex flex-col transition-all duration-300 ease-in-out"
      :class="isSidebarExpanded ? 'w-80' : 'w-20'"
    >
      <!-- Logo and Toggle -->
      <div class="flex items-center justify-between mb-8">
        <div class="flex items-center space-x-3" v-if="isSidebarExpanded">
          <div class="w-10 h-10 bg-gradient-to-br from-purple-600 to-indigo-600 rounded-xl shadow-lg flex items-center justify-center">
            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 4v16M17 4v16M3 8h4m10 0h4M3 12h18M3 16h4m10 0h4M4 20h16a1 1 0 001-1V5a1 1 0 00-1-1H4a1 1 0 00-1 1v14a1 1 0 001 1z"/>
            </svg>
          </div>
          <div>
            <h1 class="text-xl font-bold text-white">Movie Bank</h1>
            <p class="text-gray-400 text-xs">Dashboard</p>
          </div>
        </div>
        <div v-else class="w-10 h-10 bg-gradient-to-br from-purple-600 to-indigo-600 rounded-xl shadow-lg flex items-center justify-center">
          <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 4v16M17 4v16M3 8h4m10 0h4M3 12h18M3 16h4m10 0h4M4 20h16a1 1 0 001-1V5a1 1 0 00-1-1H4a1 1 0 00-1 1v14a1 1 0 001 1z"/>
          </svg>
        </div>
        
        <button
          @click="toggleSidebar"
          class="p-1 rounded-lg hover:bg-gray-700 transition-colors duration-200"
          :class="isSidebarExpanded ? '' : 'ml-auto'"
        >
          <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path v-if="isSidebarExpanded" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>
            <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
          </svg>
        </button>
      </div>

      <!-- Quick Actions Sidebar -->
      <div class="space-y-3 flex-1">
        <!-- Profile Card -->
        <div 
          class="bg-gray-750 rounded-xl p-3 hover:bg-gray-700 transition-colors duration-200 cursor-pointer group flex items-center"
          @mouseenter="hoverItem = 'profile'"
          @mouseleave="hoverItem = null"
        >
          <div class="w-8 h-8 bg-purple-600 rounded-lg flex items-center justify-center flex-shrink-0">
            <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z"/>
            </svg>
          </div>
          <div class="ml-3 overflow-hidden transition-all duration-200" :class="isSidebarExpanded ? 'w-auto opacity-100' : 'w-0 opacity-0'">
            <h3 class="text-white font-medium text-sm group-hover:text-purple-300 transition-colors whitespace-nowrap">Your Profile</h3>
            <p class="text-gray-400 text-xs whitespace-nowrap">View account details</p>
          </div>
          <!-- Tooltip for collapsed state -->
          <div v-if="!isSidebarExpanded && hoverItem === 'profile'" class="absolute left-full ml-3 px-2 py-1 bg-gray-700 text-white text-sm rounded shadow-lg whitespace-nowrap z-50">
            Your Profile
          </div>
        </div>

        <!-- Favorites Card -->
        <div 
          class="bg-gray-750 rounded-xl p-3 hover:bg-gray-700 transition-colors duration-200 cursor-pointer group flex items-center"
          @mouseenter="hoverItem = 'favorites'"
          @mouseleave="hoverItem = null"
        >
          <div class="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center flex-shrink-0">
            <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
            </svg>
          </div>
          <div class="ml-3 overflow-hidden transition-all duration-200" :class="isSidebarExpanded ? 'w-auto opacity-100' : 'w-0 opacity-0'">
            <h3 class="text-white font-medium text-sm group-hover:text-blue-300 transition-colors whitespace-nowrap">Favorites</h3>
            <p class="text-gray-400 text-xs whitespace-nowrap">Your loved movies</p>
          </div>
          <!-- Tooltip for collapsed state -->
          <div v-if="!isSidebarExpanded && hoverItem === 'favorites'" class="absolute left-full ml-3 px-2 py-1 bg-gray-700 text-white text-sm rounded shadow-lg whitespace-nowrap z-50">
            Favorites
          </div>
        </div>

        <!-- Watchlist Card -->
        <div 
          class="bg-gray-750 rounded-xl p-3 hover:bg-gray-700 transition-colors duration-200 cursor-pointer group flex items-center"
          @mouseenter="hoverItem = 'watchlist'"
          @mouseleave="hoverItem = null"
        >
          <div class="w-8 h-8 bg-green-600 rounded-lg flex items-center justify-center flex-shrink-0">
            <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/>
            </svg>
          </div>
          <div class="ml-3 overflow-hidden transition-all duration-200" :class="isSidebarExpanded ? 'w-auto opacity-100' : 'w-0 opacity-0'">
            <h3 class="text-white font-medium text-sm group-hover:text-green-300 transition-colors whitespace-nowrap">Watchlist</h3>
            <p class="text-gray-400 text-xs whitespace-nowrap">Movies to watch later</p>
          </div>
          <!-- Tooltip for collapsed state -->
          <div v-if="!isSidebarExpanded && hoverItem === 'watchlist'" class="absolute left-full ml-3 px-2 py-1 bg-gray-700 text-white text-sm rounded shadow-lg whitespace-nowrap z-50">
            Watchlist
          </div>
        </div>

        <!-- Collections Card -->
        <div 
          class="bg-gray-750 rounded-xl p-3 hover:bg-gray-700 transition-colors duration-200 cursor-pointer group flex items-center"
          @mouseenter="hoverItem = 'collections'"
          @mouseleave="hoverItem = null"
        >
          <div class="w-8 h-8 bg-yellow-600 rounded-lg flex items-center justify-center flex-shrink-0">
            <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"/>
            </svg>
          </div>
          <div class="ml-3 overflow-hidden transition-all duration-200" :class="isSidebarExpanded ? 'w-auto opacity-100' : 'w-0 opacity-0'">
            <h3 class="text-white font-medium text-sm group-hover:text-yellow-300 transition-colors whitespace-nowrap">Collections</h3>
            <p class="text-gray-400 text-xs whitespace-nowrap">Your movie lists</p>
          </div>
          <!-- Tooltip for collapsed state -->
          <div v-if="!isSidebarExpanded && hoverItem === 'collections'" class="absolute left-full ml-3 px-2 py-1 bg-gray-700 text-white text-sm rounded shadow-lg whitespace-nowrap z-50">
            Collections
          </div>
        </div>

        <!-- Ratings Card -->
        <div 
          class="bg-gray-750 rounded-xl p-3 hover:bg-gray-700 transition-colors duration-200 cursor-pointer group flex items-center"
          @mouseenter="hoverItem = 'ratings'"
          @mouseleave="hoverItem = null"
        >
          <div class="w-8 h-8 bg-red-600 rounded-lg flex items-center justify-center flex-shrink-0">
            <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"/>
            </svg>
          </div>
          <div class="ml-3 overflow-hidden transition-all duration-200" :class="isSidebarExpanded ? 'w-auto opacity-100' : 'w-0 opacity-0'">
            <h3 class="text-white font-medium text-sm group-hover:text-red-300 transition-colors whitespace-nowrap">Ratings</h3>
            <p class="text-gray-400 text-xs whitespace-nowrap">Your rated movies</p>
          </div>
          <!-- Tooltip for collapsed state -->
          <div v-if="!isSidebarExpanded && hoverItem === 'ratings'" class="absolute left-full ml-3 px-2 py-1 bg-gray-700 text-white text-sm rounded shadow-lg whitespace-nowrap z-50">
            Ratings
          </div>
        </div>
      </div>

      <!-- Logout Button -->
      <div class="pt-6 border-t border-gray-700 mt-auto">
        <button
          @click="handleLogout"
          class="w-full bg-gray-700 hover:bg-gray-600 text-gray-300 px-4 py-3 rounded-xl transition-colors duration-200 flex items-center justify-center space-x-2"
          :class="isSidebarExpanded ? '' : 'px-3'"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"/>
          </svg>
          <span class="text-sm transition-all duration-200" :class="isSidebarExpanded ? 'opacity-100' : 'opacity-0 absolute'">Logout</span>
          <div v-if="!isSidebarExpanded" class="absolute left-full ml-3 px-2 py-1 bg-gray-700 text-white text-sm rounded shadow-lg whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity duration-200">
            Logout
          </div>
        </button>
      </div>
    </div>

    <!-- Main Content -->
    <div class="flex-1 p-6 overflow-auto">
      <div class="max-w-6xl mx-auto">
        <!-- Welcome Section -->
        <div class="bg-gray-800 rounded-2xl p-6 mb-8 border border-gray-700">
          <h2 class="text-xl font-semibold text-white mb-2">🎉 Welcome to Movie Bank!</h2>
          <p class="text-gray-400">You are successfully logged in. Start exploring movies!</p>
        </div>

        <!-- Search Section -->
        <div class="bg-gray-800 rounded-2xl p-6 mb-8 border border-gray-700">
          <h2 class="text-lg font-semibold text-white mb-4">🔍 Search Movies</h2>
          <form @submit.prevent="handleSearch" class="space-y-4">
            <div class="relative">
              <input 
                type="text" 
                v-model="searchQuery" 
                placeholder="Search for movies..."
                :disabled="searchLoading"
                class="w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent transition-all duration-200 placeholder-gray-400 text-white"
              />
              <div class="absolute inset-y-0 right-0 flex items-center pr-3">
                <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
                </svg>
              </div>
            </div>
            <button
              type="submit"
              :disabled="searchLoading || !searchQuery.trim()"
              class="w-full bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-700 hover:to-indigo-700 disabled:from-gray-600 disabled:to-gray-700 text-white py-3 px-4 rounded-lg font-medium transition-all duration-200 disabled:opacity-50"
            >
              {{ searchLoading ? 'Searching...' : 'Search Movies' }}
            </button>
          </form>
        </div>

        <!-- Search Results -->
        <div v-if="searchResults" class="bg-gray-800 rounded-2xl p-6 mb-8 border border-gray-700">
          <div class="flex items-center justify-between mb-4">
            <h3 class="text-lg font-semibold text-white">
              Search Results ({{ searchResults.total_count }} found)
            </h3>
            <button
              @click="logResultsToConsole"
              class="bg-gray-700 hover:bg-gray-600 text-gray-300 px-3 py-1 rounded text-sm transition-colors duration-200"
            >
              Log to Console
            </button>
          </div>

          <div v-if="searchResults.results.length === 0" class="text-center py-8">
            <svg class="w-12 h-12 text-gray-500 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
            <p class="text-gray-400">No movies found. Try a different search term.</p>
          </div>

          <div v-else class="space-y-4">
            <div v-for="(movie, index) in searchResults.results" :key="index" class="bg-gray-700 p-4 rounded-lg">
              <h4 class="text-white font-medium mb-2">{{ movie.title }}</h4>
              <p class="text-gray-400 text-sm mb-2 line-clamp-2">{{ movie.description }}</p>
              <div class="flex items-center space-x-4 text-xs text-gray-500">
                <span>⭐ {{ movie.vote_average }}/10</span>
                <span>👥 {{ movie.vote_count }} votes</span>
                <span v-if="movie.release_date">
                  📅 {{ new Date(movie.release_date).getFullYear() }}
                </span>
              </div>
            </div>
          </div>
        </div>

        <!-- User Profile Section -->
        <div v-if="userProfile" class="bg-gray-800 rounded-2xl p-6 border border-gray-700">
          <h2 class="text-lg font-semibold text-white mb-4">👤 User Profile</h2>
          <div class="bg-gray-700 rounded-lg p-4">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
              <div>
                <span class="text-gray-400">Name:</span>
                <p class="text-white">{{ userProfile.name }}</p>
              </div>
              <div>
                <span class="text-gray-400">Email:</span>
                <p class="text-white">{{ userProfile.email }}</p>
              </div>
              <div>
                <span class="text-gray-400">Member since:</span>
                <p class="text-white">{{ new Date(userProfile.created_at).toLocaleDateString() }}</p>
              </div>
              <div>
                <span class="text-gray-400">User ID:</span>
                <p class="text-white font-mono text-xs">{{ userProfile.id }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
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
const isSidebarExpanded = ref(false)
const hoverItem = ref<string | null>(null)
const router = useRouter()

const toggleSidebar = () => {
  isSidebarExpanded.value = !isSidebarExpanded.value
}

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

<style scoped>
/* Smooth transitions */
input, button {
  transition: all 0.2s ease-in-out;
}

/* Custom focus styles */
input:focus {
  box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.3);
}

/* Line clamp utility */
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

/* Hover effect for sidebar cards */
.bg-gray-750 {
  background-color: #374151;
}

/* Ensure tooltips are positioned correctly */
.relative {
  position: relative;
}

.absolute {
  position: absolute;
}

.z-50 {
  z-index: 50;
}
</style>