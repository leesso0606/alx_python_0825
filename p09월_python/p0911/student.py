class Student():

    def __init__(self,*a):
        if len(a)==5:
            self.no=a[0] #self.no:클래스에 있는 변수 / no:함수 내에 있는 지역변수, 매개변수->self 없으면 함수내에서만 돔
            self.name=a[1]
            self.kor=a[2]
            self.eng=a[3]
            self.math=a[4]
            self.total=self.kor+self.eng+self.math
            self.avg=self.total/3
            self.rank=0
        elif len(a)==8:
            self.no=a[0] 
            self.name=a[1]
            self.kor=a[2]
            self.eng=a[3]
            self.math=a[4]
            self.total=a[5]
            self.avg=a[6]
            self.rank=a[7]

    def __str__(self):
        return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}\t{self.rank}"

    def s_total(self):
        self.total=self.kor+self.eng+self.math

    def s_avg(self):
        self.avg=self.total/3

    def s_data(self):
        return f"{self.no},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg:.2f},{self.rank}"