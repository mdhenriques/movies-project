// src/services/movieService.ts
import api from './api'

export const movieService = {
  login: (credentials: { email: string; password: string }) =>
    api.post('/auth/login', credentials),

  register: (userData: { name: string; email: string; password: string }) =>
    api.post('/auth/register', userData),

  getProfile: () => api.get('/auth/me'),

  searchMovies: (query: string, page: number = 1, limit: number = 20) =>
    api.get(`/search/movies?q=${encodeURIComponent(query)}&page=${page}&limit=${limit}`),

}
  
export default movieService