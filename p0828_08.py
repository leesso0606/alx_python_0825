# 날짜함수
import datetime
import random



# 램덤 5개
a=random.randint(1,45)
arr=random.sample(range(1,46),5) #1-45까지 중복없이 5개 가져옴
print(arr)



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
