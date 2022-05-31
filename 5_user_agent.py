import requests # requests 모듈 사용
url = "https://ohoraming.github.io/"
"""
User_Agent 값은 ("https://www.whatismybrowser.com/detect/what-is-my-user-agent/) 이곳에서 받아올 수 있음
url에 접속할 때, User_Agent 값을 넘겨주게 됨
User_Agent 값을 주기 전에는 해당 사이트에서 정보 전달을 차단할 수 있음
"""
headers = {"User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"}
res = requests.get(url, headers=headers) # 원하는 url정보를 넘겨줌
res.raise_for_status() # 올바르게 html문서를 가지고 오지 않으면 error냄

with open("myblog.html", "w", encoding="utf8") as f:
    f.write(res.text)