# 타입 확인
a = 100
b = 10.1
c = "안녕"
d = True
# c가 무슨타입?
# 타입 확인 방법 type(a)
print(type(a)) #int
print(type(b)) #float
print(type(c)) #str
print(type(d)) #bool

print("{},{}".format(1,2,3,4,5))
# .format 값이 {}보다 많아도 상관 없음. 하지만 {} 값이 .format보다 적으면 안됨.


#변수를 왜 사용하냐

# a = 10
# b = 5
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b) #2.0
# print(a//b) # 몫2
# print(a%b) #나머지 0
# print(a**b) #제곱100000

# print(10+5)
# print(10-5)
# print(10*5)
# print(10/5)
# print(10//5) # 몫2
# print(10%5) #나머지 0
# print(10**5) #제곱100000

# print(9+4)
# print(9-4)
# print(9*4)
# print(9/4)
# print(9//4) #몫 2
# print(9%4) #나머지 1
# print(9**4) #제곱6561




# 변수는 어떠한 값을 저장하는 메모리 공간(그릇), 타입은 값을 입력할 때 정해짐
# 타입 : 총 4개. 정수타입, 실수타입, 문자열타입, 불타입
# 변수선언은 그릇을 준비하는 것

a = 10   # 숫자형 타입- 정수타입
b = 10.1 # 숫자형 타입 - 실수타입, 소수점이 있으니까.
aa = "안뇽" # 문자열타입 
abc = True # 불타입(bool) - True, False / boolean

# True = 1 은 에러남. print=1 등 예약어는 별수로 사용 불가능.