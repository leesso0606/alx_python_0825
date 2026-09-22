import requests
from bs4 import BeautifulSoup
import os

url="https://www.melon.com/chart/index.htm"
headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}

# requests.get()은 해당 URL에 HTTP GET 요청을 보내서 서버의 응답을 받아오는 것
# headers=headers는 서버에게 "나는 이런 브라우저에서 접속하고 있어"라고 요청 정보를 같이 보내는 부분

res=requests.get(url,headers=headers)
res.raise_for_status() #에러시 종료
# print(res.text) #url의 html을 출력가능

soup=BeautifulSoup(res.text,'lxml') #html을 BeautifulSoup으로 분석하기 쉽게 변환

# # 파일저장
# with open('melon1.html','w',encoding='utf-8') as f:
#     f.write(res.text)
# with open('melon2.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())
# print("저장 완료")


# print("-"*50)
# s_tbody=soup.tbody
# trs=s_tbody.find_all("tr") #순위권 곡 정보, 리스트타입
# for i in range(len(trs)):
#     tds=trs[i].find_all("td")
#     rank=tds[1].find("div").get_text() #순위
#     img=tds[3].find("img")["src"] #이미지 주소를 가져오는것.
#     # ------------------------------------------------------
#     # 이미지 파일 저장하기
#     img_res=requests.get(img,headers=headers)

#     with open(f"melon_2026_{i+1}.jpg","wb") as f:
#         f.write(img_res.content)
#     # ------------------------------------------------
        
#     s_title=tds[5].find("a").get_text() #곡제목
#     artist=tds[5].find("div",{"class":"ellipsis rank02"}).get_text() #아티스트 이름
#     art_a=tds[6].find("a").get_text()#앨범명

#     print(f"순위:{rank}\n이미지:{img}\n곡제목:{s_title}\n아티스트:{artist}\t앨범명:{art_a}")


# 선생님이 하신것
s_tbody=soup.tbody
trs=s_tbody.find_all("tr") #타입 list
for idx,tr in enumerate(trs):
    tds=tr.find_all("td")
    try:
        print("순위:",tds[1].find("span",{"class":"rank"}).get_text()+"위")
        img=tds[3].find("img")["src"]
        print("이미지 링크:",img) #[],attrs

        # -----------------------------------------------
        # img정보를 가지고 호출을 다시 해야 함.--img의 정보 파일을 가져옴
        os.makedirs("./melon_img",exist_ok=True) #exist_ok:폴더가 존재하면 무시
        img_res=requests.get(img,headers=headers)

        with open(f"melon_img/melon_2026_{idx+1}.jpg","wb") as f:
            f.write(img_res.content)
        # ----------------------------------------------------

        s_as=tds[5].find_all("a")
        print("제목명:",s_as[0].get_text())#노래제목
        print("가수명:",s_as[1].get_text())#가수명
        print("앨범명:",tds[6].find("a").get_text()) #앨범명
        print("-"*50)
    except Exception as e:
        print(e)
    

print("완료")

