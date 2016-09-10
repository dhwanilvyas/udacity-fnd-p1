import requests
import json
import movie
import view

movies = []

# The API Url
url = 'https://api.themoviedb.org/3/movie/popular?api_key=7b7239657b20c59003be4fdd339956cf'

# Call the url
response = requests.get(url)

# Parse json data
data = json.loads(response.content)

# Create Movie instance for all the movies returned in the response
for d in data['results']:
    movies.append(movie.Movie(d['title'], d['poster_path'], d['id']))

# Pass the movies to the main function to render them
view.main(movies)
