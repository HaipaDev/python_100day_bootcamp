from bs4 import BeautifulSoup
import requests

URL="https://empireonline.com/movies/features/best-movies-2"

response=requests.get(URL)
website_html=response.text

soup=BeautifulSoup(website_html,"html.parser")
#print(soup.prettify())

elements=soup.find_all(name="h3",class_="listicleItem_listicle-item__title__hW_Kn")
movie_titles=[element.getText() for element in elements]
print(movie_titles)

with open("movies.txt","w") as file:
    for movie in movie_titles[::-1]:
        file.write(f"{movie}\n")