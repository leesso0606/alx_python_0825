
import random


# 6개를 입력받아 있는지 확인하시오

# 로또번호
lotto = random.sample(range(1,46),6)
print("로또번호:",lotto)

# # 입력 6개
# myNum=[]
# for i in range(6):
#     no = int(input("숫자입력:"))
#     myNum.append(no)

# # 맞는지 확인
# answer=[]
# count=0
# for i in myNum:
#     if i in lotto:
#         count=count+1
#         answer.append(i)

# # 답 출력

# print("로또번호:",lotto)
# print("입력한 번호:",myNum)
# print("정답번호:",answer)
# print("정답개수:",count)

# -------------------------------------------------

#  위 for문을 while로 바꾼것.
myNum=[]
i=0
while i<6:
    no=int(input("숫자입력:")) #1,2,3, 1
    if no not in myNum:
        myNum.append(no)
        i=i+1
    else:
        print("번호가 중복되었습니다.")

#  정답확인 부분
answer=[]
count=0
for i in myNum:
    if i in lotto:
        count=count+1
        answer.append(i)
    
print("로또번호:",lotto)
print("입력번호:",myNum)
print("정답번호:",answer)
print("정답개수:",count)



# -----------------------------------------------------

# import random
# # 1개 랜덤
# a=random.randint(1,45)
# print(a)
# # 리스트를 섞어줌
# alist=list(range(1,46))
# random.shuffle(alist)
# print(alist)

# # 랜덤으로 개수만큼 추출-중복없음
# ranArr=random.sample(range(1,46),6)
# print(ranArr)

# # 랜덤으로 개수만큼 추출-중복가능
# ranArr2=random.choices(range(1,46),k=6)
# print(ranArr2)




# --------------------------------------------------------------

# 번호는 6번 써야하는데.
# myNum = []
# for i in range(6):
#     no=int(input("숫자입력:"))
#     if no not in myNum:
#         myNum.append(no)
#     else: 
#         print("번호가 있습니다.") #숫자가 중복될 경우 5번밖에 입력 못함



# i=0
# while i<5:
#     no=int(input("숫자입력:"))
#     if no not in myNum:
#             myNum.append(no)
#             i=i+1
#     else:
#         print("번호가 있습니다.")

# print("입력 숫자:",myNum)