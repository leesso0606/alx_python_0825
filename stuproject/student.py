# 클래스는 한 파일에 한 클래스만 넣는다. 그래서 안 섞이고 관리도 편함

class Student:
    # no=0
    # name=""
    # kor=0
    # eng=0
    # math=0
    # total=0
    # avg=0
    # rank=0

    # 생성자가 있으니 위 변수는 필요 없음
    def __init__(self,*args): 
        if len(args)==5: #학생성적입력에서 객체 넣기 할때
            self.no=args[0] #no
            self.name=args[1] #name
            self.kor=args[2] #kor
            self.eng=args[3] #eng
            self.math=args[4] #math
            self.total=self.kor+self.eng+self.math
            self.avg=self.total/3
            self.rank=0
        elif len(args)==8: #stu.txt 파일에서 객체 넣기 할때
            self.no=args[0] #no
            self.name=args[1] #name
            self.kor=args[2] #kor
            self.eng=args[3] #eng
            self.math=args[4] #math
            self.total=args[5]
            self.avg=args[6]
            self.rank=args[7]



    # 문자열 함수 : print()로 바로 출력할 수 있게 해줌
    def __str__(self):
        return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}\t{self.rank}"

    # 합계 : 다른 수를 수정했을 때 합계도 고쳐줌
    def s_total(self):
        self.total=self.kor+self.eng+self.math

    # 평균 : 다른 수를 수정했을 때 평균도 고쳐줌
    def s_avg(self):
        self.avg=self.total/3

    def s_str(self):
        return f"{self.no},{self.name},{self.kor},{self.eng},{self.math},{self.total},{self.avg:.2f},{self.rank}"
