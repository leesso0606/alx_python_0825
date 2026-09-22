
# # 클래스는 한 파일에 한 클래스만 넣는다. 그래서 안 섞이고 관리도 편함

# class Student:
#     # no=0
#     # name=""
#     # total=0

#     # 생성자는 반드시 필요. 매개변수 개수 일치
#     def __init__(self,no,name,kor,eng,math):
#         # self.no=no #캡슐화 : 클래스 내부에서만 값을 수정가능
#         # 캡슐화시 값을 수정할 수 있도록 setter와 getter를 만들어줌.

#         self.no=no #self.변수: self를 안넣으면 안에서만 돌아감. self를 넣어 바깥에 있는 no에 입력/ 위 값이 없으면 만들어서 입력
#         self.name=name
#         self.kor=kor
#         self.eng=eng
#         self.math=math
#         self.total=kor+eng+math
#         self.avg=self.total/3
#         # self.rank=rank

#     # 한번에 출력할 수 있는 함수
#     def __str__(self):
#         return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}"

#     def cal_total(self):
#         self.total=self.kor+self.eng+self.math

#     def cla_avg(self):
#         self.avg=self.total/3




# # 객체 선언을 하면
# s1=Student() #s->3개 변수가 생성됨.->변수를 계속 작성할 필요 없음.
# no=1
# name="홍길동"
# total=50

# 객체 선언시 바로 값 입력
s1=Student(1,"홍길동",90,90,100)
s2=Student(2,"유관순",100,100,99)

# 출력: 참고변수명.변수명
print(s1.name)

# 수정: 참고변수명.변수명=수정값
s1.name="홍길자"
print(s1.name)

# 추가: 참고변수명.변수명 :없는 변수 입력시 추가
# s1에만 추가됨, s2등 다른 객체에 추가하고 싶으면 class에 넣어야함.
s1.rank=1
print(s1.rank)

# 전체출력
print(s1.no,s1.name,s1.kor,s1.eng,s1.math,s1.total,s1.avg,sep="\t")
print(s2)

# 수정
s1.kor=10
s1.cal_total() #== s1.total=s1.kor+s1.eng+s1.math 와 같은 말.
s1.cla_avg() #== s1.avg=s1.total/3 와 같은말
print(s1)