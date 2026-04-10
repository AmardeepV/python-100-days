from bs4 import BeautifulSoup
import requests

movie_website = requests.get(
    "https://editorial.rottentomatoes.com/guide/best-movies-21st-century/")
website_data = movie_website.text

movie_html = BeautifulSoup(website_data, 'html.parser')
movie_detais = movie_html.find_all(
    'a', class_="meta-title")
movies = [each.get_text() for each in movie_detais]

movie_data = ""
for count, movie in enumerate(movies, start=1):
    movie_data += f"{count}) {movie}\n"

with open("top_100_movies.txt", 'w') as file:
    file.write(movie_data)
