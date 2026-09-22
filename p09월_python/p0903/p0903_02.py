

# num=input("숫자입력(1/3)")
# # 앞에 숫자에는 10을 곱하고, 뒤에는 숫자에는 100을 곱하고
# # 합계를 구하시오.
# # 1*10+3*100=310

# num2=num.split("/") #['1','3']
# num2=[int(i) for i in num2] #리스트내포->int로 변경.
# print(int(num2[0])*10+int(num2[1])*100)






# --------------------------------------------------------

# >> 함수
def cal(choice):
    choice2=choice.split("/") #['1','3']:문자열
    choice2[0]=int(choice2[0])
    choice2[1]=int(choice2[1]) # int 로 변경하니 아래 choice 를 정수로 입력.

    if choice2[0]==1: #choice2가 문자열이니 ""가 필요
        print("컴퓨터",choice2[1],"개를 구매하셨습니다.")
        print("구매금액:",int(choice2[1])*1_000_000,"원")

    elif choice2[0]==2:
        print("세탁기",choice2[1],"개를 구매하셨습니다.")
        print("구매금액:",int(choice2[1])*2_000_000)
        
    else:
        print("오디오",choice2[1],"개를 구매하셨습니다.")
        print("구매금액:",int(choice2[1])*500_000)  












# >> 프로그램 시작
print("1. 컴퓨터-1_000_000") #숫가 단위가 커질 때 천단위를 _사용하여 표기가능
print("2. 세탁기-2_000_000")
print("3. 오디오-500_000")
choice=input("원하는 번호와 개수 입력(1/3)") # 1/3:1번 3개 구매함./문자열


# 함수호출
cal(choice)