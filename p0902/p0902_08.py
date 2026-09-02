
# 함수사용 이유
# 1. 중복되는 코드 재사용
# 2. 코드를 간결하게 하기 위해
# 3. 

#  func파일과 연결됨.
from func import*

# 시작위치----->
while True:
        choice=main() #ctrl누른채로 함수 누르면 함수코드로 이동.
        result=ran_number(choice)
        print("결과값:",result)