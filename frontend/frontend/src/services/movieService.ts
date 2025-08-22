// src/services/movieService.ts
import api from './api'

export const movieService = {
  login: (credentials: { email: string; password: string }) =>
    api.post('/auth/login', credentials),
  
  register: (userData: { name: string; email: string; password: string }) =>
    api.post('/auth/register', userData),
  
  getProfile: () => api.get('/auth/me'),
}

export default movieService