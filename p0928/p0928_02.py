from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv

# 1.requests파일 가져오기
# url="https://nol.yanolja.com/discovery/list/PRODUCT_CATEGORY_KOREA_ACCOMMODATION/HOTEL/900584"
# headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}

# res=requests.get(url,headers=headers)
# res.raise_for_status() #에러시 종료

# soup=BeautifulSoup(res.text,'lxml')
# print("-"*60)

# # 2. selenium:자동화 도구-스크롤 없이 가져옴
# url = "https://nol.yanolja.com/discovery/list/PRODUCT_CATEGORY_KOREA_ACCOMMODATION/HOTEL/900584"
# options = Options()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
# options.add_argument("--disable-blink-features=AutomationControlled")
# browser = webdriver.Chrome(options=options)
# browser.maximize_window() # 화면 최대창 확대

# # 브라우저 열기
# browser.get(url)
# time.sleep(2)
# # 파일 저장
# soup = BeautifulSoup(browser.page_source,'lxml') #실제로 로딩된 HTML 전체를 BeautifulSoup이 분석할 수 있도록 만듬
#                                                 #브라우저에 현재 로딩된 HTML 소스를 가져옴+HTML을 해석하는 파서
# with open('p0928/file/ya1.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify()) # 현재 가져온 html을 보기 좋게 정리해서 파일로 저장한다

# # 2-2. selenium:자동화 도구-스크롤 사용
# url = "https://www.yeogi.com/domestic-accommodations?keyword=%EC%A0%9C%EC%A3%BC&checkIn=2026-09-28&checkOut=2026-09-29&personal=2&typoCorrect=true&nonAffiliated=true"
# options = Options()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
# options.add_argument("--disable-blink-features=AutomationControlled")
# browser = webdriver.Chrome(options=options)
# browser.maximize_window() # 화면 최대창 확대
# browser.get(url)
# time.sleep(2)
# # 스크롤 추가
# # execute_script:자바스크립트 언어 사용 가능
# # 현재 스크롤 높이 가져옴
# prev_height=browser.execute_script("return document.body.scrollHeight")

# while True:
#     # 스크롤 높이 출력
#     print('높이:',prev_height)
#     # 스크롤 내리기
#     browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#     time.sleep(2)
#     # 스크롤이 추가 되었는지 확인
#     next_prev_height=browser.execute_script("return document.body.scrollHeight")
#     if prev_height==next_prev_height:
#         break
#     prev_height=next_prev_height
# # input()

# # 파일 저장
# soup = BeautifulSoup(browser.page_source,'lxml') #실제로 로딩된 HTML 전체를 BeautifulSoup이 분석할 수 있도록 만듬
#                                                 #브라우저에 현재 로딩된 HTML 소스를 가져옴+HTML을 해석하는 파서
# with open('p0928/file/yeo1.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify()) # 현재 가져온 html을 보기 좋게 정리해서 파일로 저장한다
# print("완료")


# 3.파일 BeautifulSoup변환
with open("p0928/file/yeo1.html","r",encoding="utf-8") as f:
    soup=BeautifulSoup(f,'lxml')
# 20만원 이상 숙소
uls=soup.find('ul',{'class':'css-y5z6rw'})
lis=uls.find_all('li',{'class':'gc-thumbnail-type-seller-card-wrapper css-13wylk3'})
for i in range(len(lis)):
    try:
        no=i+1
        # 숙소 이미지
        img=lis[i].find('img')['src']
        # 숙소명
        title=lis[i].find('h3',{'class':'gc-thumbnail-type-seller-card-title css-1gsfgy5'}).get_text(strip=True)
        # 가격
        price=lis[i].find('span',{'class':'css-1llao6q'}).get_text(strip=True).replace(",","")
        y_price=int(price)
        # 평점
        star=float(lis[i].find('span',{'class':'css-ry30z7'}).get_text(strip=True))
    except Exception as e:
        pass

        
    if y_price>200000 and star>9.5:
        print(no,img,title,star,y_price)
        print("-"*40)
