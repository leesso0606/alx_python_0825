#  
import random
from gugudan import*
# form gugudan import gugudan_func

def main():
    print("1. 1-10까지 숫자 맞추기 프로그램")
    print("2. 구구단 출력 프로그램")
    print("3. 두수를 입력 받아 +,-,*,/ 결과값 출력 프로그램")
    choice=int(input("원하는 번호입력:"))

    return choice

# 1. 1-10까지 숫자 맞추기 프로그램
def number_func():
    no1=random.randint(1,10)
    no2=[]
    no3=0
    while True:
        no3=int(input("1-10 사이 숫자 입력:"))
        no2.append(no3)
        if no1==no3:
            print("정답!")
            break
        elif no3>no1:
            print(no3,"보다 작은수입니다.")
        else:
            print(no3,"보다 큰수 입니다.")
    print("입력한 모든 리스트:",no2)
    print("정답:",no1)


# # 2. 구구단 출력 프로그램
# def gugudan_fucn():
#     for i in range(2,10):
#         for j in range(1,10):
#             print("{}X{}={}".format(i,j,i*j))


# 3. 두수를 입력 받아 +,-,*,/ 결과값 출력 프로그램
def cal_fucn():
    num1=int(input("첫번째 숫자를 입력하시오."))
    num2=int(input("두번째 숫자를 입력하시오."))
    str1=input("+,-,*,/ 중 1개를 입력하시오.")
    sum1=0 #변수
    if str1=="+":
                sum1=num1+num2
    elif str1=="-":
                sum1=num1-num2
    elif str1=="*":
                sum1=num1*num2
    else:
                sum1=num1/num2
    print("결과값:",sum1)

    


# 시작위치

while True:
    # 메인 출력
    choice=main()

    if choice==1:
        # 숫자 맞추기 함수
        number_func()



    elif choice==2:
        # 구구단 함수
        gugudan_fucn()

    else:
        cal_fucn()