# test2.txt파일을 읽어와서
# sut=[]
# 데이터를 리스트에 저장하시오.

stu=[]

# with : f.close() 생략가능
# with f=open("C:/aaa/test2.txt","r",encoding="utf-8") as f:


f=open("C:/aaa/test2.txt","r",encoding="utf-8")
while True:
    line=f.readline() #1줄출력
    if line=="":break # 공백일 경우 멈추고 다시 처음으로
    line=line.strip()
    print(line,end="")

    # 읽어지는 글에 ,를 없애야함
    arr=line.split(",") # arr은 리스트 형식으로 됨

    # 리스트안 딕셔너리 형태로 전황
    for i,a in enumerate(arr): # i번째 a의 값
        if 5>=i>=2:
            arr[i]=int(a)
        elif i==6:
            arr[i]=float(a)

    stu.append({'no':arr[0],'name':arr[1],'kor':arr[2],'eng':arr[3],'math':arr[4],'total':arr[5],'avg':arr[6]})
    # arr[0]은 이미 문자열 타입이라 ""을 붙일필요 없음.
    

f.close()
print(stu)
