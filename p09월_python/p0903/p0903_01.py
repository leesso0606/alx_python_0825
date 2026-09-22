# 함수의 형식: 함수명()
# 함수선언: def 파일명()
# 함수호출: print() -> def가 있어야 선언.


# 함수사용이유: 코드 재사용, 코드 간결, 오류찾기 쉬움
# c,자바 : 컴파일러 언어-모든 소스를 기계어로 번역 후 프로그램 진행 / 함수위치 상관없음
# 파이썬:스크립트 언어 -한줄씩 기계어로 번역 후 프로그램 진행 / 함수 위치가 위에 있어야 함/ 아래에 있으면 실행 안됨.

# 함수 -> 위에 있어야함.
def d_print1():
    for i in range(1,11):
        print(i)

def hello_print():
    print("안녕하세요.")
    print("안녕하세요.")
    print("안녕하세요.")
    print("안녕하세요.")
    print("안녕하세요.")

def cal(n1,n2): 
    r1=n1+n2
    r2=n1-n2
    r3=n1*n2
    r4=n1/n2
    return r1,r2,r3,r4
    # 파이썬은 리턴값이 여러개 있어도 가능

# >> 실행시점
d_print1()

hello_print()

# 보내는 건 매개변수, 받는건 return 값
n1=int(input("숫자입력:"))
n2=int(input("숫자입력:"))
r1,r2,r3,r4=cal(n1,n2) # 위 매개변수와 개수가 같아야 함/ 명이 달라도 실행은 되지만 통일하는 것이 좋음.
print(r1,r2,r3,r4)
# print("{}+{}={}".format(n1,n2,n1+n2))
# print("{}-{}={}".format(n1,n2,n1-n2))
# print("{}*{}={}".format(n1,n2,n1*n2))
# print("{}/{}={}".format(n1,n2,n1/n2))