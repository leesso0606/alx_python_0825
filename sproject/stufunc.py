stuList = []
title = ["번호","이름","국어","영어","수학","합계","평균","등수"]
s_title = ["no","name","kor","eng","math","total","avg","rank"]
stuNum = 1  #전역변수


#  저장된 파일 불러오기
def readStu():
    global stuNum
    with open("c:/aaa/stu.txt","r",encoding="utf-8") as f:
        while True:
            data=f.readline()
            if data=="":break

            data1=data.split(",")
            for i,s in enumerate(data1):
                if i==0 or i==1:
                    continue
                elif 2<=i<5:
                    data1[i]=int(s.strip())
                elif i==6:
                    data1[i]=float(s.strip())
                elif i==7:
                    data1[i]=int(s.strip())
            stuList.append(dict(zip(s_title,data1)))
            stuNum=len(stuList)+1





# 0. 메인화면 함수
def main_screen():
    print("[학생성적 프로그램]")
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    print("3. 학생성적수정")
    print("8. 학생 등수")
    print("9. 학생성적저장")
    print("0. 프로그램 종료")
    choice=int(input("숫자를 입력하시오."))
    return choice

# 1. 학생성적입력
def stu_input():
    global stuNum
    print()
    while True:
        print("[학생성적입력]")
        no=stuNum
        name=input(f"{stuNum}.학생이름(0. 이전페이지 이동):")
        if name=="0": break
        kor=int(input("국어점수"))
        eng=int(input("영어점수"))
        math=int(input("수학점수"))
        total=kor+eng+math
        avg=total/3
        rank=0

        stuList.append({'no':no,'name':name,'kor':kor,'eng':eng,'math':math,'total':total,'avg':avg,'rank':rank})
        print(f"{stuNum}.{name}학생성적이 저장되었습니다.")
        stuNum+=1
        print()

# 2. 학생성적 출력
def stu_output():
    print()
    print("[학생성적 출력]")
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*title))
    print("-"*60)
    for s in stuList:
        print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
    print()
# 3. 학생성적 수정
def stu_updata():
    print("[학생성적수정]")
    name=input("학생이름 검색:")
    temp=0
    for s in stuList:
        if s['name']==name:
            temp=1
            print(f"{name}학생이 검색되었습니다.")
            print("[수정과목]")
            print("1.국어 2.영어 3.수학")
            choice=int(input("과목을 선택하시오.(0.취소)"))
            if choice==0:
                break
            elif choice==1:
                print("[국어점수 수정]")
                print(f"현재국어점수 :{s['kor']}")
                s['kor']=int(input("변경점수입력:"))
                s['total']=s['kor']+s['eng']+s['math']
                s['avg']=s['total']/3
            elif choice==2:
                print("[영어점수 수정]")
                print(f"현재영어점수 :{s['eng']}")
                s['eng']=int(input("변경점수입력:"))
                s['total']=s['kor']+s['eng']+s['math']
                s['avg']=s['total']/3
            elif choice==3:
                print("[국어수학 수정]")
                print(f"현재수학점수 :{s['math']}")
                s['math']=int(input("변경점수입력:"))
                s['total']=s['kor']+s['eng']+s['math']
                s['avg']=s['total']/3
            print("수정이 완료되었습니다.")
            
    # 바깥으로 안빼면 없다고도 출력됨
    if temp==0:
        print(f"{name}학생이 없습니다.")
# 8. 학생 등수

# 9. 학생성적 저장
def writeStu():
    with open("c:/aaa/stu.txt","w",encoding="utf-8") as f:
        for s in stuList:
            data=(f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']:.2f},{s['rank']}")
            f.write(data+"\n")
        print("성적파일이 저장되었습니다.")