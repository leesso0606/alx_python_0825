
# 함수1번
def cal1():
    print(" [ 구구단 ] ")
    for i in range(2,10):
        for j in range(1,10):
            print("{}X{}={}".format(i,j,i*j))



# 함수 2번
def cal2():
    num1=int(input("첫번째 숫자를 입력하시오."))
    num2=int(input("두번째 숫자를 입력하시오."))
    str1=input("+,- 중 1개를 입력하시오.")
    if str1=="+":
        print("값:",num1+num2)
    else:
        print("값:",num1-num2)

# 함수 3번
def cal3():
    sum=0
    for i in range(1,11):
        sum=sum+i
        print("합:",sum)





# >>프로그램 실행.


print("1. 구구단 출력")
print("2. 두 수를 입력받아 +,- 값을 출력")
print("3. 1-10까지 합을 출력")
choice=int(input("원하는 번호를 입력하세요>>"))


if choice==1:
    cal1()
elif choice==2:
    cal2()

else:
    cal3()
    