title=["번호","이름","국어","영어","수학","합계","평균"]
k_title=['no','name','kor','eng','math','total','avg']

stu=[] #리스트 안 딕셔너리
s_no=1 #학생성적인원변수 - 나중에 DB에서 번호부여

# >>>>>>>>>>>>>>>>>프로그램 실행

# 1. 성적프로그램 메인화면
while True:
    print("[학생성적프로그램]")
    print("1.학생성적입력")
    print("2.학생성적출력")
    print("3.학생성적수정")
    print("-"*60)
    choice=int(input("실행할 프로그램 번호를 입력하시오."))

    # 학생성적입력
    if choice==1:
        while True:
            print("[학생성적입력]")
            no=s_no #번호자동으로 부여하려고
            name=input(f"{no}번째 이름 입력(0.이전화면):")
            if name=="0":
                break
            kor=int(input("국어점수"))
            eng=int(input("영어점수"))
            math=int(input("수학점수"))
            total=kor+eng+math
            avg=total/3
            stu.append({'no':no,'name':name,'kor':kor,'eng':eng,'math':math,'total':total,'avg':avg})
            print(f"{name} 학생성적이 입력되었습니다.")
            s_no=s_no+1
            print()

    # 학생성적출력
    elif choice==2:
        print("[학생성적출력]")
        print("-"*60)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-"*60)
        if len(stu)==0:
            print("저장된 학생 성적이 없습니다.")
        for s in stu:
            print(f"{s["no"]}번\t{s["name"]}\t{s["kor"]}\t{s["eng"]}\t{s["math"]}\t{s["total"]}\t{s["avg"]:.2f}")
    # 학생성적수정
    else:
        print("[학생성적 수정]")
        name=input("점수를 수정할 학생이름을 입력하시오.")
        temp=0
        for i,s in enumerate(stu):
            if s["name"]==name:
                print(f"{i+1}.{s["name"]}학생을 찾았습니다.")
                temp=1
                break
        if temp==0:
            print(f"{name}학생이 없습니다.")

        elif temp==1:
            print("[수정과목선택]")
            print("1.국어  2.영어  3.수학")
            choice=int(input("수정과목 숫자를 입력하시오."))

            if choice==1:
                print(f"현재 {title[choice+1]} 점수: {s[k_title[choice+1]]}점")
                s["kor"]=int(input("변경하려는 국어점수:"))
                s["total"]=s["kor"]+s["eng"]+s["math"]
                s["avg"]=s["total"]/3
                print(f"{s["kor"]}점으로 국어점수가 변경되었습니다.")
            elif choice==2:
                print(f"현재 영어 점수: {s["eng"]}점")
                s["eng"]=int(input("변경하려는 영어점수:"))
                s["total"]=s["kor"]+s["eng"]+s["math"]
                s["avg"]=s["total"]/3
                print(f"{s["eng"]}점으로 국어점수가 변경되었습니다.")
            else:
                print(f"현재 수학 점수: {s["math"]}점")  
                s["math"]=int(input("변경하려는 수학점수:"))
                s["total"]=s["kor"]+s["eng"]+s["math"]
                s["avg"]=s["total"]/3
                print(f"{s["math"]}점으로 국어점수가 변경되었습니다.")