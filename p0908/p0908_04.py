class Student:

    def __init__(self,no,name,kor,eng,math):
        self.no=no
        self.name=name
        self.kor=kor
        self.eng=eng
        self.math=math
        self.total=kor+eng+math
        self.avg=(kor+eng+math)/3

    def cla_total(self):
        self.total=self.kor+self.eng+self.math
    def cal_avg(self):
        self.cal_avg=self.total/3

    def print(self):
        print(self.no,self.name,self.kor,self.eng,self.math,self.total,f"{self.avg:.2f}",sep="\t")


stuList=[]
s=Student(1,"홍길동",100,100,99)
stuList.append(s)
s.kor=70
s.math=100
s.print()