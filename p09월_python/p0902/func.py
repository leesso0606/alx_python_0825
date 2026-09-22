# 함수 모음집.

import random
def ran_number(choice):
    if choice==1:
            #랜덤번호 5개
            result=random.sample(range(1,101),5)
    elif choice==2:
            # 랜덤번호 3개
            result=random.sample(range(1,101),3)
    else:
            #랜덤번호 1개.
            result=random.sample(range(1,101),1)
    return result

def main():
    print("1.랜던숫자 5개 가져오기")
    print("2.랜던숫자 3개 가져오기")
    print("3.랜던숫자 1개 가져오기")
    choice=int(input("원하는 번호를 입력하세요.>>"))
    return choice