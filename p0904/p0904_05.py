
# 파일 저장하기


stu = []
f = open("C:/aaa/test2.txt","r",encoding="utf-8")
while True:
    line = f.readline() # 1줄출력 , /n 줄바꿈때문에 에러가 남.
    if line=="": break
    line = line.strip() #앞뒤공백제거
    print(line,end="") # enter을 없앤다.

    arr = line.split(",")

    for i,a in enumerate(arr):
        if 5>=i>=2:
            arr[i] = int(a)
        elif i==6:
            arr[i] = float(a)
    # stu 리스트에 저장
    # print(arr)
    stu.append({'no':arr[0],'name':arr[1],'kor':arr[2],'eng':arr[3],'math':arr[4],'total':arr[5],'avg':arr[6]})


f.close()
print(stu)







# stu=[]

# f=open("C://aaa/test2.txt","r",encoding="utf-8")
# while True:
#     line= f.readline()
#     if line=="":break
#     line = line.strip()
#     # print(line,end="") # enter을 없앤다.

#     # 1,홍길동,100,100,100,300,100.0
#     # 문자열을 각각 문자열로 분리
#     arr=line.split(",")
#     # print(arr)

#     for i,a in enumerate(arr):
#         if 2<=i<=5:
#             arr[i]=int(a)
#         elif i==6:
#             arr[i]=float(a)
#     # stu리스트에 저장.
#     stu.append({"no":arr[0],"name":arr[1],"kor":arr[2],"eng":arr[3],"math":arr[4],"total":arr[5],"avg":arr[6]})
#     # arr[0]은 이미 문자열처리됨
#     print(arr)
#     # print(line,end="")
# f.close()
