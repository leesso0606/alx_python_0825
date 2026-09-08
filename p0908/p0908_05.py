class Student:
    def __init__(self,no,name,kor,eng,math):
        self.no=no
        self.name=name
        self.kor=kor
        self.eng=eng
        self.math=math
        self.total=kor+eng+math
        self.avg=(kor+eng+math)/3

    def __str__(self):
        return f"{self.no}\t{self.name} \t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}"

    def cal_sum(self):
        self.total=self.kor+self.eng+self.math

    def cal_avg(self):
        self.avg=self.total/3


# ------------------------
# 리스트를 클래스로 변경
class Students:
    slist=[]

    # 생성자:객체 선언시 실행됨.
    def __init__(self,s):
        self.slist.append(s)

    # 함수: 함수 호출시 실행됨
    def add(self,s):
        self.slist.append(s)




# --------------프로그램

# # 객체선언
# s=Student(1,"홍길동",100,100,99)
# s2=Student(2,"유관순",90,90,91)

#Students 객체선언
stu=Students(Student(1,"홍길동",100,100,99))

#Students 객체함수 호출
stu.add(Student(2,"유관순",90,90,91))

for ss in stu.slist:
    print(ss)





# ------------------------------------------------------


# StuList=[]

# s=Student(1,"홍길동",100,100,99)
# print(s)
# # 점수를 수정하면,sum과 avg도 함께 변경이 되어야함
# s.kor=50
# s.cal_sum()
# s.cal_avg()
# print(s)


# --------------------------------------


# while True:
#     no=input("번호:")
#     name=input("이름:")
#     kor=int(input("국어:"))
#     eng=int(input("영어:"))
#     math=int(input("수학:"))
#     stuList.append(Student(no,name,kor,eng,math))

#     for s in stuList:
#         print(s)
