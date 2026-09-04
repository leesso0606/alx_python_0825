# raise: 강제 에러 발생 


choice=int(input("원하는 번호 입력:"))
if choice==1:
    print("학생성적입력부분")
elif choice==2:
    print("수정")
elif choice==3:
    print("수정")
else:
    raise NotImplementedError #이 기능은 아직 구현하지 않았으니 에러를 발생시킨다



# ------------------------------------


# # 예외처리 try-except->없을수록 좋다.

# print(1)
# try: # 에러가 날 수 있는 코드
#     print(2)
#     print(3)
#     # print(10/0) #에러가남. ->에러가 나면 아래것. 에러가 안나면 try 식 그대로 출력.
#     print(5)
# except Exception as e: #  오류발생시 실행하는 코드 ->에러인 이유 나옴
#     print(e)
#     print(type(e))
#     print(7)
# #print(8)
# finally: # 무조건 실행하는 코트
#     print(9)



# ----------------------------------


# print(1)
# # pront(1) #구문오류-처음부터 오류

# # 런타임에러 - 진행중 틀릴때 
# arr=[1,2,3,4,5]
# while True:
#     choice=int(input("0번에서 4까지 숫자입력:"))
#     if choice.isdigit():
#         choice=int(choice)
#     else:
#         print("숫자만 입력가능합니다. 디시 입력하시오.")
#         continue
#     print("선택값:",arr[choice])
    # try:
    #     choice=int(input("0번에서 4까지 숫자입력:"))
    #     print("선택값:",arr[choice])
    # except Exception as e:->어디 부분에서 에러가 나는지 알 수 있음.
    #     print("에러발생")
    #     print(e)
    # # if choice>4:
    # #     print("잘못입력하셨습니다. 다시입력하세요.")
    # #     continue #숫자를 잘못 입력해도 다시 시작.
    # # print("선택값:",arr[choice])