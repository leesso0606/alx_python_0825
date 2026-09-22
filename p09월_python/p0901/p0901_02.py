# 1-100사이의 숫자 맞추기
# 1. 랜덤번호 1개 생성
# 2. 무한으로 입력받기(while)
# 3. 숫자를 입력받기
# 4. 랜덤번호와 숫자 비교
# 5. 결과출력

# 안보고 해보기

# 1. 
import random
a=random.randint(1,100)

# 2.

num=0 #내가 입력할 숫자
num_arr=[] #리스트
while True:
    num=int(input("숫자를 입력하시오."))
    num_arr.append(num)
    if num==a:
        print("정답입니다.")
        break #무한으로 반복되는 걸 멈춤
    elif num>a:
        print(num,"보다 작은수입니다.")
    else:
        print(num,"보다 큰수 입니다.")

print("입력한 숫자:",num_arr)
print("정답:",a)