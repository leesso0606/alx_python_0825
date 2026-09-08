
stuList = []
title = ["번호","이름","국어","영어","수학","합계","평균","등수"]
s_title = ["no","name","kor","eng","math","total","avg","rank"]
stuNum = 1  #전역변수


# 파일 불러오기
def readStu():
    global stuNum
    with open("c:/aaa/stu.txt","r",encoding="utf-8") as f:
        while True: #여러 정보가 있으니 반복해서 진행하라
            data=f.readline() 
            if data=="":
                break
            stu=data.split(",")
            for i,s in enumerate(stu):
                if 2<=i<=5:
                    stu[i]=int(s.strip())
                elif i==6:
                    stu[i]=float(s.strip())
                elif i==7:
                    stu[i]=int(s.strip())
                else: continue
            stuList.append(dict(zip(s_title,stu)))
            stuNum=len(stuList)+1
        
# zip()  → 데이터를 짝짓기
# dict() → 짝지어진 데이터를 딕셔너리로 만들기
# append() → 만들어진 딕셔너리를 리스트에 넣기
# for s in stu: ->값만 필요할때
# for i, s in enumerate(stu): -> 순서와 값 둘다 필요할때






# 메인화면
def main():
    print("[학생성적 프로그램]")
    print("1. 성적입력")
    print("2. 성적출력")
    print("3. 성적수정")
    print("9. 성적파일저장")
    print("0. 프로그램종료")
    choice=int(input("번호입력: "))
    return choice

# choice=1/ 성적입력
def stu_input():
    while True:
        global stuNum
        print("[학생성적입력]")
        no=stuNum
        name=input(f"{stuNum}번.학생이름(0:이전페이지):")
        if name=="0":
            break
        kor=int(input("국어점수:"))
        eng=int(input("영어점수:"))
        math=int(input("수학점수:"))
        total=kor+eng+math
        avg=total/3
        rank=0
        stuList.append({'no':no,'name':name,'kor':kor,'eng':eng,'math':math,'total':total,'avg':avg,'rank':rank})
        print(f"{stuNum}번.{name}학생 성적이 입력되었습니다.")
        stuNum+=1

# choice=2 /  성적 출력
def stu_output():
    print("[학생성적출력]")
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
    print("-"*60)
    for s in stuList:
        print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']}\t{s['rank']}")


# choice=9 /파일 저장
def writeStu():
    with open("c:/aaa/stu.txt","w",encoding="utf=8") as f:
        for s in stuList:
            data=(f"{s['no']},{s['name']},{s['kor']},{s['eng']},{s['math']},{s['total']},{s['avg']:.2f},{s['rank']}")
            # 리스트 안 딕셔너리를 문자열로 분해
            f.write(data+"\n")
        print("성적파일이 저장되었습니다.")