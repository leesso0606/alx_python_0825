# 웹 스크랩핑
import requests

res=requests.get("https://www.melon.com/")
res.raise_for_status() #에러가 나면 프로그램을 자동종료 시킴
print(res.text) #모든 데이터 읽어오기
print("응답 코드:",res.status_code)
print("프로그램을 종료합니다")
# print("html소스:",res.text)