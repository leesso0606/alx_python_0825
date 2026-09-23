import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# # 2. selenium:자동화 도구-크롬 드라이브가 꼭 있어야함
# browser = webdriver.Chrome()
# url = "https://stock.naver.com/market/stock/kr/stocklist/priceTop"
# # 브라우저 열기
# browser.get(url)
# time.sleep(4)
# # 파일 저장
# soup = BeautifulSoup(browser.page_source,'lxml') #실제로 로딩된 HTML 전체를 BeautifulSoup이 분석할 수 있도록 만듬
#                                                 #브라우저에 현재 로딩된 HTML 소스를 가져옴+HTML을 해석하는 파서
# with open('stock1.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify()) # 현재 가져온 html을 보기 좋게 정리해서 melon2.html파일로 저장한다


# 파일 BeautifulSoup으로 변환
# 파일을 읽기 모드(r)로 열고, 
# 그 파일의 HTML 내용을 BeautifulSoup에 전달해서 lxml 파서로 HTML 구조를 분석할 수 있도록 만든다.
with open("stock1.html","r",encoding="utf-8") as f:
    soup=BeautifulSoup(f,'lxml')

# 파싱 시작
s_headTitle=[] #상단제목추가
s_tr=soup.thead.tr
ths=s_tr.find_all('th')
for th in ths:
    s_headTitle.append(th.get_text(strip=True))
    # print(th.get_text(strip=True))
print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*s_headTitle))
print("-"*85)


# 표 정보
s_tbody=soup.tbody
# trs=s_tbody.find("tr") #find:첫번째것만 가져옴-sk하이닉스정보
trs=s_tbody.find_all("tr") #모든 tr정보-100개정보
for tr in trs:
    tds=tr.find_all("td") #td 8개 전부
    s_index=tds[0].find("span",{"class":"index"}).get_text(strip=True) #순위
    s_title=tds[0].find("span",{"class":"SingleLineText_text__HI_cb"})
    s_title=s_title.get_text(strip=True) #공백을 제거하여 text만 가져와라 #종목명
    s_price=tds[1].find("span",{'class':'SingleLinePrice_price__g_6VV'})
    s_price=s_price.get_text(strip=True) #현재가
    s_align=tds[2].find("span",{"class":"ModulePriceChange_amount__4QYMz"}).get_text(strip=True) #전일대비
    s_volume=tds[3].find("span",{"class":"SingleLinePrice_single-line-price__bnpQv SingleLinePrice_medium__QoN_F"}).get_text(strip=True) #거래량
    s_prices=tds[4].find("span",{"class":"SingleLinePrice_single-line-price__bnpQv SingleLinePrice_medium__QoN_F"}).get_text(strip=True) #거래대금
    s_high=tds[5].find("span",{'class':'SingleLinePrice_price__g_6VV'}).get_text(strip=True) #고가
    s_row=tds[6].find("span",{"class":"SingleLinePrice_price__g_6VV"}).get_text(strip=True) #저가
    s_money=tds[7].find('span',{"class":"SingleLineText_text__HI_cb"})
    s_money=s_money.get_text(strip=True) #총액
    print(f"{s_index}.\t{s_title}\t{s_price}\t{s_align}\t{s_volume}\t{s_prices}\t{s_high}\t{s_row}\t{s_money}")
    
    





# ------------------------------------------------------------------

# # 1.requests
# # 단점: 자바스크립트로 구동되는 소스 가져올 수 없다.
# # requests정보 가져오기->css문법 변환->find,find_all() 
# url="https://www.melon.com/chart/index.htm"
# headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
# # User-Agent:Python-requests정보
# res=requests.get(url,headers=headers)
# res.raise_for_status() #에러시 종료
# # css문법변환
# soup=BeautifulSoup(res.text,'lxml')


