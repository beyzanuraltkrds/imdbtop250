import requests
from bs4 import BeautifulSoup
import re

url = "https://www.imdb.com/chart/top/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
response = requests.get(url, headers=headers)

html_content = response.content
soup = BeautifulSoup(html_content, "html.parser")

a = float(input("Enter the rating:"))

movies = soup.find_all("div", {"class": "ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b85248f1-7 lhgKeb cli-title"})
ratings = soup.find_all("span", {"class": "ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating"})

for movie, rating in zip(movies, ratings):
    movie = movie.text.strip()


    rating_text = rating.text
    imdb_rating = re.search(r'\d+\.\d+', rating_text)
    if imdb_rating:
        rating_value = float(imdb_rating.group())  #
        if rating_value > a:
            print("Name of the movie: {}  Rating of the movie: {}".format(movie, rating_value))
