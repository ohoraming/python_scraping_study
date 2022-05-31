import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=651673"

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("td", attrs={"class": "title"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]

# 웹툰 제목과 링크 출력
for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com" + cartoon.a["href"]
    # print(title, link)

# 별점 평균 구하기
ratings = soup.find_all("div", attrs={"class": "rating_type"})
star_sum = 0.0
for rating in ratings:
    star = rating.strong.get_text()
    star_sum += float(star)

star_average = star_sum / len(ratings)
print('Average:', star_average)
