# 날짜함수
import datetime
import random


a=[1,2,3,4,5]
print(a) #[1, 2, 3, 4, 5]
a[2]=30
a[3]=500
print(a) #[1, 2, 30, 500, 5]
a.pop(2)
print(a) #[1, 2, 500, 5]
# 뒤에추가
a.append(200) 
print(a) #[1, 2, 500, 5, 200]






# --------------------------------------


# # 1-45가지 랜덤 5개를 가져와서
# # 입력한 숫자가 있으면 당첨, 없으면 꽝
# # 1개만 우선
# # 5개
# lotto=random.sample(range(1,46),5)
# print(lotto)
# iarr=[]

# # 반복문
# for i in range(5):
#     iarr.append(int(input("숫자입력:")))
# # 비교해서 있으면 당첨, 없으면 꽝
# for i in range(5):
#     if iarr[i] in lotto:print("당첨")
#     else: print("꽝")



# input1=int(input("숫자입력: "))
# input2=int(input("숫자입력: "))
# input3=int(input("숫자입력: "))
# input4=int(input("숫자입력: "))
# input5=int(input("숫자입력: "))

# if input1 in lotto:
#     print("당첨")
# else:
#     print("꽝")
# if input2 in lotto:
#     print("당첨")
# else:
#     print("꽝")
# if input3 in lotto:
#     print("당첨")
# else:
#     print("꽝")
# if input4 in lotto:
#     print("당첨")
# else:
#     print("꽝")
# if input5 in lotto:
#     print("당첨")
# else:
#     print("꽝")






# ----------------------------------------

# # 램덤 5개
# # randint-랜덤1개, sample-랜덤여러개(중복불가),
# # shuffle-전체섞음, choices-랜덤여러개(중복가능)
# a=random.randint(1,45)
# arr=random.sample(range(1,46),5) #1-45까지 중복없이 5개 가져옴
# print(arr)
# arr2=random.sample([1,2,3],2)
# print(arr2)
# # 리스트 전체를 랜덤으로 섞어줌.
# arr3=[1,2,3,4,5]
# random.shuffle(arr3)
# print(arr3)

# arr4=[1,2,3,4,5]
# arr5=random.choices(arr4,k=5) #리스트 해당개수만큼 가져옴, 중복가능
# print(arr5)



# -------------------------------------------

# # 리스트 생성방법
# a=random.randint(1,45)
# alist1=[0,0,0,0,0]
# alist2=[0]*5
# alist3=list(range(1,6)) #range는 범위를 정함.
# print(alist1) #[0, 0, 0, 0, 0]
# print(alist2) #[0, 0, 0, 0, 0]
# print(alist3) #[1, 2, 3, 4, 5]


# ---------------------------------------


# # 
# now=datetime.datetime.now()
# # year,month,day,hour,minute,second
# print(now)
# print(now.year)
# print(now.month)

# # random
# r_num=random.randint(1,12)
# # 3,4,5 봄/ 6,7,8 여름/ 9,10,11 가을/12,1,2 겨울

# if r_num>=3:
#     print("봄")
# elif r_num>=6:
#     print("여름")
# elif 12>r_num and r_num>9: #12>r_num>=9
#     print("가을")
# else:
#     print("겨울")

# # now.month
# # 01월,02월...
