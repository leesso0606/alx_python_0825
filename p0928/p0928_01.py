from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv



# # 2-2. selenium:자동화 도구-스크롤 사용

# url="https://flight.naver.com/flights/domestic/SEL:city-CJU:airport-20261006/CJU:airport-SEL:city-20261008?adult=1&fareType=YC"
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
# with open('p0928/file/flight2.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify()) # 현재 가져온 html을 보기 좋게 정리해서 파일로 저장한다
# print("완료")

# 3.파일 BeautifulSoup변환
with open("p0928/file/flight2.html","r",encoding="utf-8") as f:
    soup=BeautifulSoup(f,'lxml')

flights=soup.find_all('div',{'class':'domestic_Flight__8bR_b'})
# print(len(flights))

# 항공권이 7만원 이하에 있는 비행기표를 출력.
for i in range(len(flights)):
    # 항공사
    airline=flights[i].find('b',{'class':'airline_name__0Tw5w'}).get_text(strip=True)
    routes=flights[i].find_all('b',{'class':'route_time__xWu7a'})
    # 출발 시간
    route1=routes[0].get_text(strip=True)
    # 도착시간
    route2=routes[1].get_text(strip=True)
    # # 가격
    price=flights[i].find('i',{'class':'domestic_num__ShOub'}).get_text(strip=True)
    f_price=int(price.replace(",",""))
    if f_price<70000:   
        print(airline,route1,route2,f_price)
        print("-"*40)




# ---------------------------------------------------------------


# # .env파일에서 읽어와서 변수값 입력
# load_dotenv()
# id=os.getenv('id')
# # id='admin' #프로그램에 노출됨
# print(id)