

def cal(num1,num2,str1):
    result=0
    if str1=="+":
        result=num1+num2
    elif str1=="-":
        result=num1-num2
    elif str1=="*":
        result=num1*num2
    else:
        result=num1/num2
    return result


num1=int(input("숫자입력:"))
num2=int(input("숫자입력:"))
str1=input("+,-,*,/ 중에 1개를 입력하세요.>>")
result=cal(num1,num2,str1)
print("결과값:",result)



# ---------------------------------------

# # 함수리턴

# def add(num1,num2):
#     sum=num1+num2
#     return sum # 호출하는 곳으로 값 전달

# while True:
#     num1=int(input("숫자입력:"))
#     num2=int(input("숫자입력:"))
#     total=add(num1,num2)
#     print("결과값:",total)



# -----------------------------------------------------------



# # 함수는 호출하는 명령어 위에 있어야 함./ 파이썬은 스크립트 언어라서 그럼.
# # 함수의 매개변수 개수가 틀리면 에러남. -> 서로 같은 것을 사용할 때 편함.
# while 에 있는 매개변수를 바꿔 함수에 영향을 끼침.

# def print1(num1,str1):
#     for i in range(num1):
#         print(i,str1)



# while True:
#     num1=int(input("숫자입력:"))
#     str1=input("출력하는 문구 입력:")
#     print1(num1,str1) #num1:매개변수
    