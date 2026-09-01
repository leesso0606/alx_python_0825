# 구구단
for i in range(2,9+1):
    for j in range(1,9+1):
        print("{}X{}={}".format(i,j,i*j))

# 1-100사이의 숫자 맞추기
# 1. 랜덤번호 1개 생성
# 2. 숫자를 입력받기 -> 무한으로 입력받기(while)
# 3. 숫자를 입력받기
# 4. 랜덤번호와 숫자 비교
# 5. 결과출력

import random
ran_no = random.randint(1,100)

# 반복문에는 for(반복적, 회수가 지정),while(조건일때, 무한)

in_no:0 #입력변수
in_arr=[] #입력한 모든 숫자 리스트 저장
while True: #무한루트
    in_no=int(input("1-100까지 숫자 입력:")) #숫자 입력
    # 입력한 숫자를 리스트에 넣기 -> 여기에 넣어야 모두 저장됨.
    in_arr.append(in_no)
    if in_no==ran_no:
        print("정답입니다.")
        break
    elif in_no>ran_no:
        print(in_no,"보다 작은수를 입력하세요")
    else:
        print(in_no,"보다 큰수를 입력하세요")

print("입력한 모든 리스트",in_arr)
print("정답:",in_arr[-1])