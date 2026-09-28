from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv
import undetected_chromedriver as uc 


# 2. selenium:자동화 도구-스크롤 없이 가져옴


url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent&traceId=muksjcx4"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "ko-KR,ko;q=0.9",
    "Referer": "https://www.coupang.com/",
}
options = uc.ChromeOptions()
options.add_argument("--no-first-run --no-service-autorun --password-store=basic")
options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36")
browser = uc.Chrome(options=options)
browser.maximize_window() # 화면 최대창 확대
# 브라우저 열기
browser.get(url)
time.sleep(2)
# 파일 저장
soup = BeautifulSoup(browser.page_source,'lxml') #실제로 로딩된 HTML 전체를 BeautifulSoup이 분석할 수 있도록 만듬 #브라우저에 현재 로딩된 HTML 소스를 가져옴+HTML을 해석하는 파서
with open('p0928/file/coupang1.html','w',encoding='utf-8') as f:
    f.write(soup.prettify()) # 현재 가져온 html을 보기 좋게 정리해서 파일로 저장한다
print("완료")
input()