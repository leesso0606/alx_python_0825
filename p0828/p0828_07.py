paper="네팔 대홍수 참사 수습이 언제 끝날지도 모르는 상황에서\
      2차 홍수가 덮칠 수 있다는 관측이 나오고 있습니다.\
      이번 홍수의 원인으로 지목된 것처럼 산 위의 빙하가 붕괴되면서\
          비 한 방울 없이 홍수가 또 일어날 수 있다는 겁니다."

a= paper.find("홍수")
print(a) #4

# find(검색내용, 시작위치, 종료위치)
b=paper.find("홍수",5)
print(b)


# # 앞에서 부터 홍수 단어가 몇번째부터 있는지 알 수있음.
# a= paper.find("홍수")
# print(a)
# # 뒤에서 부터 홍수 단어가 몇번째부터 있는지 알수있음.
# b= paper.rfind("홍수")
# print(b)
# # 글에 홍수가 몇번 나왔는지 알수있음.
# c=paper.count("홍수")
# print(c)

## 홍수라는 글자가 어디어디에 있는지 위치를 알고 싶어요.
# 반복문 사용하여 진행.





# -------------------------------

# print("[ 로그인 페이지 ]")
# while(True):
#     id=input("아이디: ")
#     pw=input("패스워드: ")
#     if id=="aaa" and pw=="1111":
#         print("로그인 성공. 메인페이지로 이동합니다.")
#         break
#     else:
#         print("아이디 또는 패스워드가 일치하지 않습니다. 다시 로그인해주세요.")
# print("메인페이지가 열립니다.")



# ----------------------------------------------------------

# name=input("이름입력:")
# kor=input("국어점수 입력: ")
# if kor.isdigit():
#     kor=int(kor)
# else:
#     print("숫자가 아닙니다. 다시 입력하세요.")
# print(name, kor)


# name=input("이름입력:")
# while(True):
#     if kor.isdigit():
#         kor=input("국어점수 입력: ")
#         break
#     else:
#         print("숫자가 아닙니다. 다시 입력하세요.")
# print(name, kor)
# # 위에것은 반복문임. 나중에 배울예정


# ------------------------------------------

# # 문자인지 아닌지 확인
# # 이름을 입력을 받는데 영문이름
# name = input("이름을 입력하세요.")

# if name.isalpha(): #특수문자나 숫자인지 확인가능
#     print("문자 알파벳으로 되어 있습니다.")
# else:
#     print("특수문자나 한글이 입력되었습니다.")
# print(name)

# --------------------------------------

num = input("숫자를 입력하세요")
if num.isdigit(): #숫자인지 확인
    num =int(num)
    num+= 100
    print("입력숫자:", num)
else:
    print(num)


# ----------------------------------------------

# # format 함수
# a=10
# print("{}".format(a))
# print("{:10d}".format(a))
# print("{:010d}".format(a))
# print("{:+010d}".format(-10)) # +:앞에 단위를 붙여줌.-000000010
# print("{:3,d}".format(12345689)) # 천단위 표시
# print("{:.2f}".format(12345689)) # 소수점 제한

