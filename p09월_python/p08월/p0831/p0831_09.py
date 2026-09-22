# 로또번호 맞추기 프로그램을 구현하시오

# 랜덤숫자 6개
import random
lotto= random.sample(range(1,46),6)
print("로또번호:",lotto)

# while문으로 내가 입력한 6개 숫자

num=[]
i=0
while i<6:
    num1=int(input("숫자를 입력하시오"))
    if num1 not in num:
        num.append(num1)
        i=i+1

print("입력숫자:",num)


# 입력 숫자와 로또 번호가 같은가?
answer=[] # 일치숫자
count=0 #일치 개수
for i in num:
    if i in lotto:
        count=count+1
        answer.append(i)

print("로또번호:",lotto)
print("맞은 번호:",answer)
print("맞은 개수:",count)





# --------------------------------------------------------------

# for 문으로 내가 입력한 6개 숫자
# num=[]

# for i in range(6):
#     num1=int(input("숫자를 입력하시오."))
#     num.append(num1)
# print("내가 입력한 숫자;",num)

# # 내가 입력한 숫자와 로또번호가 몇개 맞았고 어떤 숫자가 맞았는지

# answer=[]
# count=0

# for a in num:
#     if a in lotto:
#         count=count+1
#         answer.append(a)

# print("맞은숫자:",answer)
# print("맞은개수:",count)

