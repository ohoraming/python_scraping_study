import requests # requests 모듈 사용

res = requests.get("https://google.com/") # 원하는 url정보를 넘겨줌
res.raise_for_status() # 올바르게 html문서를 가지고 오지 않으면 error냄

# res = requests.get("https://www.naver.com/") # 원하는 url정보를 넘겨줌
# print("응답코드: ", res.status_code) # 200이면 정상 

# 이렇게 if문을 쓰지 않고 raise_for_status()를 사용함
# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)