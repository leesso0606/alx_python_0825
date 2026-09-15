
stu=[]
title=["번호","이름","국어","수학","영어","합계","평균","등수"]
s_title = ["no","name","kor","eng","math","total","avg","rank"]
sno=1


# 파일 불러오기
def readlist():
    global sno
    with open ("c:/aaa/stu.txt","r",encoding="utf-8") as f:
        while True:
            data=f.readline()
            if data=="":break

            data1=data.split(",")
            for i,v in enumerate(data1):
                if i==0 or i==1:
                    continue
                elif 2<=i<=5:
                    data1[i]=int(v.strip())
                elif i==6:
                    data1[i]=float(v.strip())
                elif i==7:
                    data1[i]=int(v.strip())
            stu.append(dict(zip(s_title,data1)))
            sno=len(stu)+1

# 메인
def main():
    while True:
        print("[학생성적프로그램]")
        print("1. 성적입력")
        print("2. 성적출력")
        print("3. 성적수정")
        print("9. 성적저장")
        choice=int(input("숫자를 입력하시오."))
        return choice

# 1. 성적입력
def s_input():
    global sno
    while True:
        print("[성적입력]")
        no=sno
        name=input(f"{sno}.이름(0.취소):")
        if name=="0":break
        kor=int(input("국어 점수:"))
        eng=int(input("영어 점수:"))
        math=int(input("수학 점수:"))
        total=kor+eng+math
        avg=total/3
        rank=0
        stu.append({'no':no,'name':name,'kor':kor,'eng':eng,'math':math,'total':total,'avg':avg,'rank':rank})
        print(f"{name}학생이 저장되었습니다.")
        sno+=1
        print()

# 2. 성적출력
def s_output():
    print("[성적출력]")
    print()
    print("-"*60)
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format("번호","이름","국어","영어","수학","합계","평균","등수"))
    print("-"*60)
    for s in stu:
        print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")

# 3. 성적 수정
def s_updata():
    print("[성적수정]")
    name=input("검색할 이름:")
    temp=0
    for i in stu:
        if i['name']==name:
            temp=1
            print(f"{name}학생이 검색되었습니다.")
            print("수정할 과목을 선택하십시오.")
            print("1.국어 2.영어 3.수학")
            choice=int(input("숫자를 선택하시오.(0.취소)"))

            if choice==0: break
            elif choice==1:
                print("현재 국어점수:",i['kor'])
                i['kor']=int(input("변경 점수:"))
                i['total']=i['kor']+i['eng']+i['math']
                i['avg']=i['total']/3
            elif choice==2:
                print("현재 영어점수:",i['eng'])
                i['eng']=int(input("변경 점수:"))
                i['total']=i['kor']+i['eng']+i['math']
                i['avg']=i['total']/3
            elif choice==3:
                print("현재 수학점수:",i['math'])
                i['math']=int(input("변경 점수:"))
                i['total']=i['kor']+i['eng']+i['math']
                i['avg']=i['total']/3
    if temp==0:
        print(f"{name}학생의 정보는 없습니다.")

# 성적 저장
def s_write():
    print("[성적저장]")
    print()
    with open("c:/aaa/stu.txt","w",encoding="utf-8") as f:
        for s in stu:
            data= f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']:.2f},{s['rank']}"
            print(data)
            f.write(data+"\n")
        print("성적이 저장되었습니다.")
