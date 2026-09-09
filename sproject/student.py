# 앞글자가 대문자면 클래스
# 클래스 내에 함수:메소드
class Student:
    # 생성자가 없으면 변수를 일일히 넣어야함
    # 생성자:객체선언시 자동으로 실행되는것.
    # 파이썬에서는 생성자 1개밖에 못만듬
    def __init__(self,no,name,kor,eng,math):
        self.no=no #self.no:클래스에 있는 변수 / no:함수 내에 있는 지역변수, 매개변수->self 없으면 함수내에서만 돔
        self.name=name
        self.kor=kor
        self.eng=eng
        self.math=math
        self.total=kor+eng+math
        self.avg=self.total/3
        self.rank=0

    def __str__(self):
        return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}\t{self.rank}"

    def s_total(self):
        self.total=self.kor+self.eng+self.math

    def s_avg(self):
        self.avg=self.total/3


# 읽어오는건 get/ 저장하는건 set을 주로 쓴다. 기억하기
# getter/setter ->@Property/@ .setter