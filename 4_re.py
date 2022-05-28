import re

p = re.compile("ca.e") # 정규식 기입

def print_match(m):
    if m:
        print("m.group():", m.group()) # 일치하는 문자열 반환, 아니면 에러발생
        print("m.string:", m.string) # 입력받은 문자열을 그대로 반환 
        print("m.start():", m.start()) # 일치하는 문자열의 시작 index
        print("m.end():", m.end()) # 일치하는 문자열의 끝 index
        print("m.span(): ", m.span()) # 일치하는 문자열의 시작/끝 index
    else:
        print("매칭되지 않음")

# m = p.match("carelese") # match: 주어진 문자열의 처음부터 일치하는지 확인
# print_match(m) 

# m = p.search("mmmcacelese") # search: 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m) 

lst = p.findall("good care cafe carre") # findall: 일치하는 모든 것을 리스트로 반환
print(lst) 

"""
1. p = re.compile("원하는 형태")
    원하는 형태: "정규식"
    . (ca.e): 하나의 문자를 의미
    ^ (^de): 문자열의 시작 (de로 시작하는 문자열)
    $ (se$): 문자열의 끝 (se로 끝나는 문자열)
2. m = p.match("비교할 문자열") 
    match(): 주어진 문자열의 처음부터 일치하는지 확인
3. m = p.search("비교할 문자열")
    search(): 주어진 문자열 중에 일치하는게 있는지 확인
4. lst = p.findall("비교할 문자열")
    findall(): 일치하는 모든 것을 "리스트"로 반환
5. 참고할만한 사이트
    https://www.w3schools.com/python/python_regex.asp
    https://docs.python.org/ko/3/library/re.html
"""