
from student import Student
from students import Students

# Students객체선언
stus=Students()

stuNum=1 #전역변수


# 학생성적 파일불러오기
def readStu():
    global stuNum
    with open("c:/aaa/stu.txt","r",encoding="utf-8") as f:
        while True:
            str=f.readline() #1,홍길동,100,100,100,300,100.0,0
            if str=="":break

            # 문자열을 분리 리스트 형태로 변경

            stu=str.split(",")
            # 타입변환
            for i,s in enumerate(stu):
                if i==0 or i==1:
                    continue
                elif 2<=i<=5:
                    stu[i]=int(s.strip())
                elif i==6:
                    stu[i]=float(s.strip())
                elif i==7:
                    stu[i]=int(s.strip())

            # Student(1."홍길동",100,100,100) 한것과 같다.
            # 클래스 추가
            # 객체 선언 후 Students리스트에 추가
            stus.add(Student(stu[0],stu[1],stu[2],stu[3],stu[4],stu[5],stu[6],stu[7]))

            # 번호추가부분
            stuNum=len(stus.slist)+1

            # -------------클래스로 바꾸고 삭제예정
            # stuList.append(dict(zip(s_title,stu)))
            # stuNum=len(stuList)+1

# zip()  → 데이터를 짝짓기
# dict() → 짝지어진 데이터를 딕셔너리로 만들기
# append() → 만들어진 딕셔너리를 리스트에 넣기
# for s in stu: ->값만 필요할때
# for i, s in enumerate(stu): -> 순서와 값 둘다 필요할때


#  학생성적 파일 저장하기
# stuList의 모든것을 파일 저장하기
def writeStu():
    with open("c:/aaa/stu.txt","w",encoding="utf-8") as f:
        for s in stus.slist:
            str= s.s_str() #Student객체의 s_str()함수 호출
            # str=(f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']:.2f},{s['rank']}")
            print(str)
            f.write(str+"\n")
        print("성적파일이 저장되었습니다.")
        print()






# 0. 메인화면 함수 선언
def main_screen():
    print("[학생성적프로그램]")
    print("1. 성적입력")
    print("2. 성적출력")
    print("3. 성적수정")
    print("9. 성적파일저장")
    print("0. 프로그램 종료")
    print("-"*60)
    choice=int(input("원하는 번호 입력:"))
    return choice

# 1.학생성적입력함수 선언 -클래스 변경 완료
def stu_input():
    global stuNum
    while True:
        print()
        print("[ 학생성적입력 ]")
        no = stuNum
        name = input(f"{stuNum}번째. 학생이름(0.이전페이지 이동) : ")
        if name == "0": break
        kor = int(input("국어 : "))
        eng = int(input("영어 : "))
        math = int(input("수학 : "))
        total = kor+eng+math
        avg = total/3
        rank = 0

        # 클래스로 넣겠다
        stus.add(Student(no,name,kor,eng,math))

        # stuList.append({'no':no,'name':name,'kor':kor,\
        #                 'eng':eng,'math':math,\
        #                     'total':total,'avg':avg,\
        #                         'rank':rank,})

        print(f"{stuNum}.{name} 학생성적이 저장되었습니다.")
        print()
        stuNum += 1
    
    

# 2.학생성적출력함수 선언 - 클래스로 변경 완료
def stu_output():
    
    # Students print()함수 출력
    stus.print()


    # print()
    # print(" "*25,end="")
    # print("[학생성적출력]")
    # print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
    # print("-"*60)
    # for s in stuList:
    #     print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
    #     print()

# 3. 학생성적 수정함수 선언
def stu_updata():
    print() #모든 정보는 stus.slite에 있다.
    print("[학생성적수정]")
    name=input("학생이름 검색: ")
    temp=0 #임시변수
    for s in stus.slist:
        if s.name==name:
            temp=1
            print(f"{name}학생이 검색되었습니다.")
            print("[수정과목]")
            print("1.국어  2.영어  3.수학")
            print("-"*60)
            choice=int(input("과목을 선택하세요.(0번은 취소)"))
            if choice==0:
                break
            elif choice==1:
                print("[국어점수변경]")
                print("현재 점수:",s.kor)
                s.kor=int(input("변경점수입력:"))
                
            elif choice==2:
                print("[영어점수변경]")
                print("현재 점수:",s.eng)
                s.eng=int(input("변경점수입력:"))
                
            elif choice==3:
                print("[수학점수변경]")
                print("현재 점수:",s.math)
                s.math=int(input("변경점수입력:"))
                
            # 공통인 값 밖으로 빼서 한번에 사용하기
            s.s_total()
            s.s_avg()
            print("수정이 완료되었습니다.")


    if temp==0:
        print(f"{name}학생이 없습니다.")

