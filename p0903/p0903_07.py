

# 모듈 가져오기.

from func import cal1,cal2,cal3 #함수 하나씩 지정하여 오픈할 수 있음.
from func import* #저장된 함수 모두를 가져옴.
cal1()
cal2()
cal3()

import datetime
now=datetime.datetime.now()
import random #도 모듈중 하나.
import sys

print(sys.builtin_module_names)

import math
dir(math)
print(math.log(10))
print(math.sin(10))
print(math.floor(10.921)) #버림
print(math.ceil(10.111)) #올림
print(round(10.541,2)) #반올림. (값,소주점자리)


# import func
# func.cal1()
# func.cal2()
# func.cal3()

# -------------------------------------------------

# # para_func()

# # 매개변수가 2개인 함수를 호출한 결과

# def para_func(a,b,*c):
#     sum=a+b
#     for n in c:
#         sum=sum+n
#     return sum


# print(para_func(1,2,3))
# print(para_func(1,2))
# print(para_func(10,20,30,40,50))


# -------------------------------------------


# # 가변매개변수

# def func1(*num):
#     sum=0
#     for n in num:
#         sum=sum+n
#     return sum


# print(func1(1,2,3))
# print(func1(1,2))
# print(func1(10,20,30,40,50))




# ------------------------------------------

# def func1(a,b,c):
#     print(a)
#     return a+10


# c=30
# result = func1(10,2,c)
# print(result) #20



# ------------------------------------------------------


# # 지역변수와 전역변수는 다른 변수이다.
# # gloal

# def func1():
#     global a # 전역변수에 선언되어 있는 링크를 가져옴
#     a =10
#     print("func1 a:",a)

# a=20
# func1()
# print("전역변수:",a)



# --------------------------------------------


# # 각 함수에 지역변수가 없으면 전역변수 가져온다.
# # 다른 함수에 있는 지역변수는 못 건들인다.

# def func1():
#     a=10 #함수 a:지역변수
#     print("func1 a:",a)

# def func2():
#     print("func2 a:",a)

# a=20 #함수 밖 a:전역변수

# # 실행
# func1() #10
# func2() #20

