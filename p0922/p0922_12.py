from selenium import webdriver #셀레니움으로 웹 브라우저를 조작하기 위한 기능
from selenium.webdriver.common.by import By #셀레니움에서 html요소를 찾을 때 어떤 기준으로 찾을지 지정
from selenium.webdriver.common.keys import Keys #키보드 입력을 셀리니움으로 보내기 위한 기능
import requests #웹사이트에 http요청을 보내는 라이브러리
from bs4 import BeautifulSoup #html을 분석하고 원하는 태그를 찾기 쉽게 만들어 주는 도구
import time #시간 조절 도구
import os #파일이나 폴더,운영체제와 관련된 작업을 할 때 사용, 파일 만들기 등

# # selenium파일 저장
# browser=webdriver.Chrome()
# url="https://stock.naver.com/market/stock/kr/stocklist/priceTop"
# browser.get(url)
# time.sleep(3)
# soup=BeautifulSoup(browser.page_source,'lxml') #브라우저에 현재 로딩된 HTML 소스를 가져옴+HTML을 해석하는 파서
# with open("naver_market.html","w",encoding="utf-8") as f:
#     f.write(soup.prettify())

# 변환한 파일 불러오기
# naver_market.html 파일을 읽기 모드(r)로 열고, 
# 그 파일의 HTML 내용을 BeautifulSoup에 전달해서 lxml 파서로 HTML 구조를 분석할 수 있도록 만든다.
with open("naver_market.html","r",encoding="utf-8") as f:
    soup=BeautifulSoup(f,'lxml')

s_tbody=soup.find("tbody",{'class':'Table_tbody__EJrOg'})
trs=s_tbody.find_all("tr")
tds=trs[0].find_all("td")
print(tds[0].find('span',{'class':'SingleLineText_text__HI_cb'}).get_text(strip=True))



