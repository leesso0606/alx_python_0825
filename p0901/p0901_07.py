# 리스트의 개념: 리스트를 활용해 음식 궁합을 출력하는 프로그램

# a,b,c,d,e=0,0,0,0,0 #에러남. 하나 추가할 때마다 추가해야함.
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)


# a_arr=[10,20,30,40,50,60,70,80,90,100]
# sum=0
# for a in a_arr:
#     print(a)
#     sum=sum+a
# print(sum) #합

# print(a_arr[2:5]) # 주소 2-4까지 / [30, 40, 50]
# print(a_arr[::-1]) # 역순 / [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]

# 리스트 추가 :append(뒤에), insert(위치), extend(리스트+리스트)
# 리스트 수정 :a_arr[위치]=1000(수정할 문자열, 숫자 등)
# 리스트 삭제 :pop(위치):위치가 없으면 제일 뒤에, del위치

# a_list = [1,2,3]
# a_list.append(4)
# print(a_list) # [1, 2, 3, 4]
# a_list.pop()
# print(a_list) # [1, 2, 3]
# a_list.pop(0) # 위치
# print(a_list) # [2, 3]


# --------------------------------------------------------

# 퀴즈
# 100이상의 숫자만 출력하시오.

n_arr = [100,91,230,1,2,5,70,500]

num=[]

for n in n_arr:
    if n>=100:
        num.append(n)
        print(n)
# 리스트 형식으로 출력하시오
print(num)

# 31:3자리숫자
# 230:2자리숫자
# 1:1자리숫자
# 숫자를 문자열타입으로 변경 /  몇자리 숫자인지 작성하시오.

num1=[]

for n in n_arr: #n타입:정수타입 -> 문자타입
    no=len(str(n))
    a="{}:{}자리숫자".format(n,no)
    num1.append(a)
    print(a)
# 리스트형식으로 출력하시오.
print(num1)


# a=100
# b="100"
# print(len(b)) #str 타입만 len 사용 가능.
# print(len(a)) # 숫자라서 개수가 문자 개수가 없음 에러남
