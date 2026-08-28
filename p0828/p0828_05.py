a=11
print(type(int(a)))

b=1.12
print(int(b)) #1. 정수만 나옴
print(float(b)) #1.12

c=10
d=3
e=10/3
e1=10//3 #나머지
print(type(e)) # <class 'float'>
print(type(e1)) #<class 'int'>

f=5
if f%2==0:print("짝수")
else:print("홀수")

result = "짝수" if f%2==0 else "홀수" #출약문
print(result)

