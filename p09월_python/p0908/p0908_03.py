

# 앞글자가 대문자면 객체로 작성./ 함수와 헷갈리지 않도록 약속임.
class Student:
    

    # 생성자
    def __init__(self,no,name,kor,eng,math):
        self.__no=no
        self.__name=name
        self.__kor=kor #캡슐화 : 클래스 내부에서만 값 수정가능
        self.__eng=eng #있으면 있는 곳에 넣어주고
        self.__math=math
        self.__total=kor+eng+math # 없는 것을 넣으면 자동으로 생성됨.
        self.__avg=(kor+eng+math)/3
    # 클래스 내의 함수 매개변수 첫번째 self꼭 넣어야함
    def cal_total(self):
        self.__total=self.__kor+self.__eng+self.__math

    def cla_avg(self):
        self.__avg=self.__total/3

    # get,set으로 캡슐화된 변수를 변경할 수 있다. 하지만 일일이 만들어야함.
    def get_kor(self):
        return self.__kor
    
    def set_kor(self,kor): #캡슐화를 하면, 잘못된 값이 입력될때 에러처리 가능
        if kor<0:
            print("잘못된 값이 들어옴.")
            return
        self.__kor=kor
    

    def print(self):
        print(self.__no,self.__name,self.__kor,self.__eng,self.__math, self.__total,f"{self.__avg:.2f}",sep="\t")

    # 변수를 print해도 아래 소스코드 내용이 출력이 된다.
    def __str__(self):
        return f"{self.__no}\t{self.__name} \t{self.__kor}\t{self.__eng}\t{self.__math}\t{self.__total}\t{self.__avg:.2f}"


    
# ---------------------------------
stuList=[]
# 객체선언
s=Student(1,"홍길동",100,100,99)
print("-"*60)
print(s)
print("-"*60)
stuList.append(s)
s.kor=70 # 클래스 변수 수정 ->있는 변수에 값을 넣으면 수정됨.
s.math=40 # 없는 변수 값을 넣으면 class에 자동으로 생성된다.
s.__math=40 # 캡슐화된 값 변경 불가능.

# set 값을 사용하여 캡슐화된 값 변경
s.set_kor(50) 
s.cla_total()
s.cal_avg()
s.print()
print(s)