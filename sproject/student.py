
class Student:

    def __init__(self,no,name,kor,eng,math):
        self.no=no
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