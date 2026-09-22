
# 파일 읽기 


# abc파일 출력
with open("C:/aaa/abc.txt","r",encoding="utf-8") as f:
    while True:
        str=f.readline()
        if str=="":break
        print(str,end="")








# -----------------------------------------------------------


# sum=0
# with open("C:/aaa/aaa.txt","r",encoding="utf-8") as f:
#     while True:
#         str=f.readline()
#         if str=="": break
#         if str.strip().isdigit(): #빈 공백제거
#             str=int(str)
#             sum=sum+str
#         print(type(str),end="")
#         print(str)

# print("합계:",sum)





# -----------------------------------------------


# stuList=[]
# # stu.txt를 출력하시오
# f=open("C:/aaa/stu.txt","r",encoding="utf-8")
# while True:
#     str=f.readline() #한줄을 읽어줘
#     if str=="": break
#     stu=str.split(",") #,를 기준으로 리스트 생성
#     for i,s in enumerate(stu): #1,홍길동,100,100,100,300,100.0

#         if i==0 or i==1: continue #문자열 그대로
#         elif 2<=i<=5:
#             stu[i]=int(s.strip())
#         elif i==6:
#             stu[i]=float(s.strip()) #빈공백 없애서 넣는다. \n이 들어가서 에러남.
#     stuList.append(stu)        
# print("파일 읽어오기 완료")
# print(stuList)
    
# f.close()







# ------------------------------------

# # with 파일 읽어오기 : colse는 필요 없음

# with open("C:/aaa/abc.txt","r",encoding="utf-8") as f: # as는 약칭 / 한글파일 읽어오기.
#     while True:
#         str=f.readline() #한줄씩 읽어오는것.
#         if str=="":break
#         print(str,end="")
    


# ----------------------------------------------


# open() 파일 읽어오기

# readFile=open("C:/aaa/abc.txt","r")
# while True:
#     str=readFile.readline() #한줄씩 읽어오는것.
#     if str=="":break
#     print(str,end="")
# readFile.close() # 오픈하면 클로즈 반드시 필요. 바깥에 있어야함.

# # print("프로그램 종료")