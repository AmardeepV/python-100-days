from bs4 import BeautifulSoup
import requests

# html_file = "website.html"

# with open(html_file) as file:
#     data = file.read()

# soup = BeautifulSoup(data, "html.parser")

# print(soup.title.string)

responce = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
data = responce.text

soup = BeautifulSoup(data, "html.parser")
stories = soup.find_all('a', class_="storylink")
score = soup.find_all('span', class_="score")

article_text = []
article_link = []
article_scores = []
for each in stories:
    article_text.append(each.get_text())
    article_link.append(each.get('href'))

article_scores = [int(each.get_text().split()[0]) for each in score]
max_score_index = article_scores.index(max(article_scores))

print(
    f"the title of the largest score is: {article_text[max_score_index]} and the link for it is: {article_link[max_score_index]}")
