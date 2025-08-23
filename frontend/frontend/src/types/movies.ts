// src/types/movie.ts
export interface MovieSearchResult {
  id: number
  title: string
  description?: string
  release_date?: string
  poster_path?: string
  vote_average?: number
  vote_count?: number
}

export interface SearchResponse {
  results: MovieSearchResult[]
  total_count: number
  page: number
  total_pages: number
}