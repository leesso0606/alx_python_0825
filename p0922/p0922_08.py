import requests
from bs4 import BeautifulSoup

url="https://www.melon.com/chart/index.htm"
headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}

res=requests.get(url,headers=headers)
res.raise_for_status() #에러시 종료

soup=BeautifulSoup(res.text,'lxml')
print("-"*50)
s_tbody=soup.tbody
trs=s_tbody.find_all("tr",{"class":"lst50"}) #곡 정보들
for i in range(50):
    tds=trs[i].find_all("td")
    rank=tds[1].find("div").get_text() #순위
    imges=tds[3].find("img")["src"] #이미지
    
    print(f"{rank}\t{imges}")