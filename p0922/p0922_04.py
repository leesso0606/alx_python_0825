import requests #웹접근
from bs4 import BeautifulSoup #html로 파싱

#headers를 넣어 웹스크래핑이 아니라 agent로 접근한다고 꾸미는 것
# url='https://www.whatismybrowser.com/detect/what-is-my-user-agent/'
# url="https://www.melon.com/chart/index.htm"
url="http://www.naver.com"
headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}

res=requests.get(url,headers=headers)
res.raise_for_status() #에러시 자동 종료
# print("에러코드:",res.status_code) #상태코드를 알 수 있음

print(res.text) #text만 가져온다

# res.text를 뽑아 파일명 stu.html로 저장한다 
with open('naver1.html','w',encoding='utf-8') as f:
    f.write(res.text)

print("저장완료")
# f=open('stu.html','w',encoding='utf-8')
# f.close()