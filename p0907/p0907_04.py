# 1.csv파일에서 아래 처럼 파일 읽어오기

m_str = '"서울특별시  (1100000000)","9,330,658","4,482,949","          2.08","4,504,432","4,826,226","          0.93"'
test=m_str.split('","')
for i,t in enumerate(test):
    t=t.replace('"','') # "를 빈공백으로 대체해줘
    t=t.replace(',','') # ,를 빈공백으로 대체해줘
    t=t.replace('','') 
    t=t.strip() # 빈 공백을 없애줘
    if t.isdigit():
        t=float(t)
        test[i]=t
    # print(type(t))
print(test)

# -------------------------------------
# 서울 전체인구에서 남성비율은 몇%인가? 출력하시오

print("서울총인구 남성비율:{:.2f}%".format(test[4]/test[1]*100))
print("서울총인구 여성비율:{:.2f}%".format(test[5]/test[1]*100))

# ---------------------------------------------------

# m_str=[]
# with open("C:/aaa/1.csv","r",encoding="ansi") as f:
#     while True:
#         str=f.readline()
#         if str=="":
#             break
#         pp=str.strip().split('","')
#         m_str.append(pp)
#     print(m_str)
