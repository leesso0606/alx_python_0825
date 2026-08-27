# 1. 1-100까지 랜덤 숫자 3개를 를 리스트에 추가
# 2. 1개 숫자를 입력 받아
# 있으면 당첨, 없으면 꽝
# 랜덤숫자 리스트 출력
# 입력숫자 출력
# import random
# arr2 = random.sample(range(1,101),3)
# arr2.sort() #순차정렬
# input1 = int(input("숫자입력 : "))
# if input1 in arr2:
#     print("당첨")
# else:
#     print("꽝")
# print("랜덤숫자 :",arr2)
# print("입력숫자 :",input1) # 선생님이 하신것.



# # 1. 3개를 리스트에 추가
import random
num1=random.randint(1,100)
num2=random.randint(1,100)
num3=random.randint(1,100)
# 중복이 있을 수 있음
arr=[num1,num2,num3]

# # 2. 
aaa=int(input("숫자를 입력하시오")) #변수로 만들어 후에 print할 것을 만듬.
# # 3.
if arr in arr:
     print("당첨")
else:
     print("꽝")

# 4.
print("랜덤숫자:",arr)
print("숫자:",aaa)


