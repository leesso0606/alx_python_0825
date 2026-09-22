# # print : 출력
# # input : 입력
# num = input ("숫자를 입력하세요.")
# print("입력숫자 :{}".format(num))

# input으로 받은 모든 것은 문자열타입.
# a = int(input("1번째 숫자를 입력하세요.")) # str타입을 int타입으로 변경
# b = int(input("2번째 숫자를 입력하세요."))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a**b) #10*10*10. 10의 3승



# 아이디, 패스워드를 입력받아 출력하시오.
# 아이디:aaa, 패스워드:1111
아이디=input("아이디를 입력하시오")
패스워드=input("패스워드를 입력하시오")
print("아이디확인 : {}".format("aaa"==아이디)) # Ture, False를 알수 있음.
print("aaa"==아이디) 
print("1111"==패스워드)
print("아이디{},패스워드:{}".format(아이디,패스워드))



# a = 10
# b =3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a**b) #10*10*10. 10의 3승


# num1=100
# num2=100
# num3=100
# print(num1,num2,num3)

# # 한줄에 여러변수에 1개의 값을 넣는 것 가능
# num4=num5=num6=1
# print(num4,num5,num6)

# # 한줄에 여러변수에 여러개 값을 넣는 것을 불가
# # a1=1, a2="안녕"
# a1=1
# a2=2
# print(a1,a2)

# no1 = 100 #변수선언과 동시에 값 전달, 대입하다
# print(10==10) # 같다 표현은 ==