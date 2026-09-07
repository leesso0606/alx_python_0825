def add():# num까지의 합 / 함수선언은 실행되지 않음.
    num=int(input("num1:숫자를 입력하시오"))
    sum=0
    for i in range(1,num+1):
        sum=sum+i
    print(sum)

# 매개변수1개
def add2(num2):# num까지의 합 / 함수선언은 실행되지 않음.
    sum=0
    for i in range(1,num2+1):
        sum=sum+i
    print(sum)
    return num2


# 매개변수2개
def add3(num3,num4):# int값을 바깥으로 빼니 return으로 다시 돌려줘야함.
    sum=0
    for i in range(num3,num4+1):
        sum=sum+i
    print(sum)
    return num3,num4

# print를 프로그램 실행으로 뺄때
def add4(num5,num6):# int값을 바깥으로 빼니 return으로 다시 돌려줘야함.
    sum=0
    for i in range(num5,num6+1):
        sum=sum+i
    return sum


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>프로그램 실행.
# 10번 반복
for i in range(10):
    add()


# 매개변수1개
for i in range(10):
    num2=int(input("num2:숫자를 입력하시오"))
    add2(num2)


# 매개변수2개
for i in range(10):
    num3=int(input("num3:숫자를 입력하시오"))
    num4=int(input("num4:숫자를 입력하시오"))
    add4(num3,num4)
    

# sum 값 출력을 함수안이 아닌 실행코드에서 하고 싶을 때
for i in range(10):
    num5=int(input("num3:숫자를 입력하시오"))
    num6=int(input("num4:숫자를 입력하시오"))
    sum=add4(num5,num6)
    print(sum)