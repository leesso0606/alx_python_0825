

# 클래스 : 변수와 함수 포함해서 구현할 수 있다.
# class 클래스명(대문자로 시작):
# 이부분에 코드작성


class Car:
    color=""
    speed=0
    tire=0
    door=0

    # 생성자/생성함수 : Car() 선언될 때 실행되는 함수
    def __init__(self,color,speed,tire,door):
        self.color=color
        self.speed=speed
        self.tire=tire
        self.door=door

    def upSpeed(self): #self는 꼭 넣어야함
        self.speed+=10

    def downSpeed(self):
        self.downSpeed-=10

# ------------------------------------------------------------------------------

# 클래스 1개 생성
c=Car() #객체(인스턴스)생성 /4개의 변수, 2개의 함수가 자동으로 만들어짐.
c.color="whiet"
c.speed=100
c.tire=5
c.door=3
c.upSpeed() # c에 들어간 클래스 안 변수만 사용 /  자기것만 사용

# 클래스 객체 선언
c2=Car("skublue",200,4,5)
c2.upSpeed()

c3=Car("gray",50,5,5)
c3.upSpeed()
