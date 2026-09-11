
# slist=[]
# title=["번호","이름","국어","수학","영어","합계","평균","등수"]
# s_title = ["no","name","kor","eng","math","total","avg","rank"]

from student import Student
from students import Students

stus=Students()
sno=1

# 파일 불러오기
def readlist():
    global sno
    with open("c:/aaa/stu.txt","r",encoding="utf-8") as f:
        while True:
            stu=f.readline()
            if stu=="":break

            data=stu.split(",")
            for i,s in enumerate(data):
                if i==0 or i==1:
                    continue
                elif 2<=i<=5:
                    data[i]=int(s.strip())
                elif i==6:
                    data[i]=float(s.strip())
                elif i==7:
                    data[i]=int(s.strip())
            stus.add(Student(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]))
            sno=len(stus.slist)+1
            # slist.append(dict(zip(s_title,data)))
            # sno=len(slist)+1


# 메인화면
def main():
    print("[학생성적프로그램]")
    print("1.성적입력")
    print("2.성적출력")
    print("3.성적수정")
    print("9.파일 저장")
    print("0.프로그램 종료")
    print("-"*60)
    choice=int(input("원하는 번호 입력"))
    return choice

# 1. 성적입력
def s_input():
    global sno
    while True:
        
        print("[성적 입력]")
        no=sno
        name=input(f"{sno}번.학생이름(0.이전화면):")
        if name=="0": break
        
        kor=int(input("국어점수:"))
        eng=int(input("영어점수:"))
        math=int(input("수학점수:"))
        total=kor+eng+math
        avg=total/3
        rank=0
        stus.add(Student(no,name,kor,eng,math))
        # slist.append({'no':no,'name':name,'kor':kor,'eng':eng,'math':math,'total':total,'avg':avg,'rank':rank})
        print(f"{sno}번{name}학생이 입력되었습니다.")
        sno+=1
        print()

# 2. 성적 출력
def s_output():
    stus.print()
    # print()
    # print("[학생 성적 출력]")
    # print("-"*60)
    # print("{}{}{}{}{}{}{}{}".format("번호","이름","국어","수학","영어","합계","평균","등수"))
    # print("-"*60)
    # for s in stus.slist:
    #     print(f"{s.no}\t{s.name}\t{s.kor}\t{s.eng}\t{s.math}\t{s.total}\t{s.avg:.2f}\t{s.rank}")


# 3. 성적 수정
def s_updata():
    print("[학생 성적 수정]")
    name=input("검색할 이름:")
    n=0
    for s in stus.slist:
        if s.name==name:
            n=1
            print(f"{name}이 검색되었습니다.")
            print("수정할 과목을 입력하시오")
            print("1.국어 2.영어 3.수학")
            choice=int(input("과목을 선택하시오(0.취소)"))
            if choice==0: break
            elif choice==1:
                print("현재 국어 점수:",s.kor)
                s.kor=int(input("변경점수:"))
                
            elif choice==2:
                print("현재 영어 점수:",s.eng)
                s.eng=int(input("변경점수:"))
                
            elif choice==3:
                print("현재 수학 점수:",s.math)
                s.math=int(input("변경점수:"))
            s.s_total()
            s.s_avg()
    if n==0:
        print(f"{name}학생이 없습니다.")

# 파일 저장하기
def s_write():
    with open("c:/aaa/stu.txt","w",encoding="utf-8") as f:
        for s in stus.slist:
            s_data=s.s_data()
            # f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']:.2f},{s['rank']}"
            print(s_data)
            f.write(s_data+"\n")
        print("성적이 저장되었습니다.")