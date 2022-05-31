import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status() # 문제 발생시 프로그램 종료

soup = BeautifulSoup(res.text, "lxml") # 위에서 받아온 HTML 문서를 lxml parser를 통해 BeautifulSoup 객체로 만듦. 즉 soup은 모든 정보를 가진 것

# soup 객체를 통해 html의 element에 바로 접근이 가능해짐
print(soup.title) # title element 가져옴 
print(soup.title.get_text()) # title의 text만 가져옴
print(soup.a) # soup 객체에서 처음 발견되는 a tag를 반환
print(soup.a.attrs) # a element의 속성을 dict 형태로 반환
print(soup.a["href"]) # 특정 속성의 값을 반환

# 해당 사이트에 대해 잘 모를 때
print(soup.find("a", attrs={"class": "Nbtn_upload"})) # class="Nbtn_upload"인 첫 번째 a element를 가져옴
print(soup.find(attrs={"class": "Nbtn_upload"})) # class="Nbtn_upload"인 첫 번째 element를 가져옴

rank1 = soup.find("li", attrs={"class": "rank01"})
print(rank1.a.get_text())
# 다음 형제 관계 element로 가기
# rank2 = rank1.next_sibling.next_sibling
# print(rank2.a.get_text())
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())

# 이전 형제 관계 element로 가기
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.get_text())

# print(rank1.parent) # 부모관계 element 반환

# 반복적인 next_sibling을 쓰지 않기 위해
# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="하루만 네가 되고 싶어-126. 저와 혼약해주십시오") # text가 조건과 같은 a element를 반환
print(webtoon)