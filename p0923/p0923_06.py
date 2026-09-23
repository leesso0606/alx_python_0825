from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv
headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}


# # 파일 저장하기
# for i in range(2016,2022):
#     m_url = f'https://search.daum.net/search?w=tot&q={i}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR'
#     # print(m_url)

#     # 2. selenium : 자동화 구현
#     # 상단 제어창문구 삭제
#     options = Options()
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     options.add_experimental_option("useAutomationExtension", False)
#     options.add_argument("--disable-blink-features=AutomationControlled")
#     browser = webdriver.Chrome(options=options)
#     browser.maximize_window() # 화면 최대창 확대
#     url = m_url
#     browser.get(url)
#     time.sleep(3)

#     soup=BeautifulSoup(browser.page_source,'lxml')
#     with open(f"p0923/file/movie_{i}.html","w",encoding="utf-8") as f:
#         f.write(soup.prettify())
#         time.sleep(2)

# /----------------------------------------------

# # 파일 BeautifulSoup변환
for idx in range(2016,2022):
    with open(f"p0923/file/movie_{idx}.html","r",encoding="utf-8") as f:
        soup=BeautifulSoup(f,'lxml')


    # with open("p0923/file/movie_2016.html","r",encoding="utf-8") as f:
    #         soup=BeautifulSoup(f,'lxml')
    m_ul=soup.find('ul',{'class':'c-list-basic ty_flow35'})
    lis=m_ul.find_all("li")

    print(f'[{idx}년 베스트 10영화]')
    for i in range(len(lis)):
        print(f'{i+1}위')
        #1.이미지 주소
        m_img=lis[i].find('img')['src']
        print(m_img)




        # 이미지 파일 저장
        # requests.get(주소):"이 주소에 접속해서 데이터를 가져와줘."
        # headers는 서버에 보내는 추가 정보 ->"이 이미지 주소에 접속할 건데, 나는 이런 브라우저에서 접속했어."
        img_res=requests.get(m_img,headers=headers)
        img_res.raise_for_status()#에러시 강제종료
        with open(f"p0923/file/movie_img/{idx}년{i+1}위.jpg","wb") as f:
            f.write(img_res.content) #이미지 파일 저장은 content,문서 파일 저장은 text




        # 2.제목
        m_title=lis[i].find('strong',{'class':'tit-g clamp-g'}).get_text(strip=True)
        print(m_title)
        # 3.누적관객수
        m_desc=lis[i].find('p',{'class':'conts-desc clamp-g'}).get_text(strip=True)
        print(int(m_desc[3:-2].replace(",","")))
        # 4.개봉날짜
        m_date=lis[i].find('span',{'class':'conts-subdesc clamp-g'}).get_text(strip=True)
        print(m_date)
        print("-"*60)

