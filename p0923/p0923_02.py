import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os
headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}

# # 2. selenium:자동화 도구-크롬 드라이브가 꼭 있어야함
# browser = webdriver.Chrome()
# url = "https://comic.naver.com/bestChallenge?sortType=starscore"
# # 브라우저 열기
# browser.get(url)
# time.sleep(4)
# # 파일 저장
# soup = BeautifulSoup(browser.page_source,'lxml') #실제로 로딩된 HTML 전체를 BeautifulSoup이 분석할 수 있도록 만듬
#                                                 #브라우저에 현재 로딩된 HTML 소스를 가져옴+HTML을 해석하는 파서
# with open('webtoon1.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify()) # 현재 가져온 html을 보기 좋게 정리해서 파일로 저장한다


# 파일 BeautifulSoup으로 변환
# 파일을 읽기 모드(r)로 열고, 
# 그 파일의 HTML 내용을 BeautifulSoup에 전달해서 lxml 파서로 HTML 구조를 분석할 수 있도록 만든다.
with open("webtoon1.html","r",encoding="utf-8") as f:
    soup=BeautifulSoup(f,'lxml')


# 정보 가져오기
s_ul=soup.find("ul",{"class":"BestChallengeView__challenge_list--sUqhh"})
lis=s_ul.find_all("li")
view_total=0
view_avg=0
for i in range(3):

    # 제목 가져오기
    s_contitle = lis[i].find('span',{'class':'ContentTitle__title--e3qXt'})
    s_title=s_contitle.find("span",{"class":"text"}).get_text(strip=True)
    print("제목:",s_title)
    # 작가 이름
    s_author=lis[i].find("a",{"class":"ContentAuthor__author--CTAAP"}).get_text(strip=True)
    print("작가:",s_author)
    # 별점:소수점이 있으니 float로 변경하여 데이터 가공
    stars=lis[i].find("span",{"class":"Rating__star_area--dFzsb"})
    s_star=float(stars.find("span",{"class":"text"}).get_text(strip=True))
    print("별점:",s_star)
    # 뷰:1,134만의 [:-1]을 넣어 끝에 문자열을 없애고 replace로 ,를 공백으로 변경->숫자로 만듬
    views=lis[i].find("span",{"class":"Rating__view_area--GQb_S"})
    s_view=int(views.find("span",{"class":"text"}).get_text(strip=True)[:-1].replace(",",""))
    view_total+=s_view
    print("뷰:",s_view)

    # 이미지 주소 가져오기
    s_img=lis[i].find("img")["src"]
    print("이미지주소:",s_img)

    # 이미지 저장
    img_res=requests.get(s_img,headers=headers)
    img_res.raise_for_status()
    # 폴더생성
    os.makedirs('./p0923/webtoon',exist_ok=True)
    
    with open(f'./p0923/webtoon/w_{i+1}.jpg','wb') as f:
        f.write(img_res.content)

view_avg=view_total/3
print(f"평균 조회수:{view_avg:.2f}만")
print("완료")


# a="1,123만원" 
# print(a[:-1]) #1,123만
# print(a[:-2]) #1,123
# print(a[-1]) #원
# print(a[-2:]) #만원
# print(int(a[:-2].replace(",",""))) #1123









# ------------------------------------------------------
# a=float("9.92")
# b=float("8.0")
# c=float("9.1")
# print((a+b+c)/3)

# aa="1,023"
# aa=int(aa.replace(",",""))
# bb="2,120"
# bb=int(bb.replace(",",""))
# cc="3,023"
# cc=int(cc.replace(",",""))
# print((aa+bb+cc)/3)
