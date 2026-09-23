from selenium import webdriver #셀레니움으로 웹 브라우저를 조작하기 위한 기능
from selenium.webdriver.common.by import By #셀레니움에서 html요소를 찾을 때 어떤 기준으로 찾을지 지정
from selenium.webdriver.common.keys import Keys #키보드 입력을 셀리니움으로 보내기 위한 기능
import requests #웹사이트에 http요청을 보내는 라이브러리
from bs4 import BeautifulSoup #html을 분석하고 원하는 태그를 찾기 쉽게 만들어 주는 도구
import time #시간 조절 도구
import os #파일이나 폴더,운영체제와 관련된 작업을 할 때 사용, 파일 만들기 등
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options





# 2. selenium:자동화 구현-크롬 드라이브가 꼭 있어야함
# elem.click():클릭
# elem.send_keys():입력창 글자 입력
# elem.send_keys(Keys.ENTER): 키보드 enter키 입력
# browser.switch_to.window(browser.window_handles[1]):두 번째 브라우저 창(또는 탭)으로 이동하는 것
# 상단 제어장 문구 삭제
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-blink-features=AutomationControlled")

browser = webdriver.Chrome(options=options)
browser = webdriver.Chrome()
browser.maximize_window
url = "https://www.naver.com/"

# 1. 검색창에 날씨라고 입력>enter>온도,날씨를 출력하시오
browser.get(url)
# 검색클릭->입력
elem1=browser.find_element(By.ID,'query')
elem1.click()
elem1.send_keys('날씨')
elem1.send_keys(Keys.ENTER)
# 온도 출력
time.sleep(3)
soup=BeautifulSoup(browser.page_source,'lxml')
temp=soup.find("div",{"class":"temperature_text"}).get_text(strip=True) #에러가 떳을때 get부분 지워서 확인.
print(temp)
input()









# -----------------------------------------------------
# # 브라우저 열기
# browser.get(url)
# browser.find_element(By.CLASS_NAME,"MyView-module__link_login___VlF7z").click()
# time.sleep(3)
# elem=browser.find_element(By.ID,'id')
# elem.send_keys('aaa') 
# elem2=browser.find_element(By.ID,"pw")
# elem2.send_keys("1111")
# input()




# ---------------------------------------
# # .env파일 읽기
# load_dotenv()
# print(os.getenv('naver_id'))












