import requests
from bs4 import BeautifulSoup

url = ""
res = requests.get(url)
res.raise_for_status()

coupang = BeautifulSoup(res.text, "lxml")

# https://youtu.be/yQ20jZwDjTE?t=6654