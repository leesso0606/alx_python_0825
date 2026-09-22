# 클래스는 한 파일에 한 클래스만 넣는다. 그래서 안 섞이고 관리도 편함

class Student:
    # no=0
    # name=""
    # total=0

    # 생성자는 반드시 필요. 매개변수 개수 일치
    def __init__(self,no,name,kor,eng,math):
        # self.no=no #캡슐화 : 클래스 내부에서만 값을 수정가능
        # 캡슐화시 값을 수정할 수 있도록 setter와 getter를 만들어줌.

        self.no=no #self.변수: self를 안넣으면 안에서만 돌아감. self를 넣어 바깥에 있는 no에 입력/ 위 값이 없으면 만들어서 입력
        self.name=name
        self.kor=kor
        self.eng=eng
        self.math=math
        self.total=kor+eng+math
        self.avg=self.total/3
        # self.rank=rank

    # 한번에 출력할 수 있는 함수
    def __str__(self):
        return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}"

    def cal_total(self):
        self.total=self.kor+self.eng+self.math

    def cla_avg(self):
        self.avg=self.total/3