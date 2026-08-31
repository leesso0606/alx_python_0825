#  1-100 사이의 랜덤 번호를 맞추는 프로그램을 구현하시오
# 랜덤 번호 보다 높은 수를 입력하면 낮은 숫자 입력!, 높은 숫자 입력! 멘트 입력
# 정답을 맞추면
# 정답숫자:
# 숫자입력 회수:
# 입력한 숫자 모두 출력


import random
# 랜덤한 숫자 범위
a=random.randint(1,100)


num=0 #내가 입력한 숫자 변수
i=[] #입력한 숫자 리스트
answer=0

while True:
    num=int(input("숫자입력:"))
    i.append(num)
    if a==num:
        print("정답")
        break
    elif a>num:
        print("높은숫자")
    else:
        print("낮은숫자:")


print("정답숫자:",a)
print("입력한 숫자:",i)