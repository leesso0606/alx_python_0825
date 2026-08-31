
# 반복문
# fori in range(10),range(1,11),range(1,11,2)/ [1,2,3]/"안녕하세요"
# 구구단 출력

# for i in range(2,10):
#     print(i,"X",1,"=",i*1)
#     print("{}X{}={}".format(i,1,i*1))
#     print(f"{i}X{1}={i*1}")

# for i in range(2,10):
#     print("[{}단]".format(i))
#     for j in range(1,10):
#         print("{}X{}={}".format(i,j,i*j),end="  ")
#     print()


for i in range(2,10):
    for j in range(1,10):
        print("{}X{}={}".format(i,j,i*j),end="\t")
    print() #빠져나왔을 때 새로운 줄로 이동된것.





# print(1,end="\t")
# print(2,end="\t")
# print(3) #123 처럼 옆으로 출력된다. ## end="" /  안 넣으면 하단으로 떨어짐.



# ----------------------------------------------------

# # for i in (리스트, range(숫자),문자열 올수 있음)
# num=[3,9,10,105,220,2,1]
# for n in num:
#     print(n)

# for i in "안녕하세요":
#     print(i)

# 입력한 숫자가 홀수인지, 짝수인지 출력하시오
# a=int(input("숫자입력"))



# if a%2==0:
#     print("짝수")
# else:
#     print("홀수")

# # 3,9:홀수, 10:짝수
# num=[3,9,10,105,220,2,1]
# for n in num:
#     # print(n)
#     # a=int(input("숫자입력:"))
#     if n%2==0:
#         print(n,":짝수")
#     else: pass #else 다음에 아무것도 없으면 에러, pass는 위 조건 외 것은 넘김.
#         # print(n,":홀수")




# ------------------------------


# for i in range(1,11):
#     print(i)

# # 1,2,3,------10->10,20,30,40,----100
# for i in range(1,11):
#     print(i*10)

# arrs=[1,3,5,7]
# for arr in arrs:
#     print(arr)

# fruits = ["사과","배","바나나"]
# for f in fruits:
#     print(f)



# ---------------------------------------------

# # # 이름입력을 3번 반복하시오
# # for i in range(3):
# #     input("이름: ")

# # [학생명단]
# # 홍길동
# # 유관순
# # 이순신 한번에 나오게 하시오
# name=[]
# a=[]
# for n in range(3):
#     a=input("이름:")
#     name.append(a) #리스트 :append, insert, extend
# print("[학생명단]")
# print(name)
# for n in name:
#     print(n)



# ----------------------------------
# for i in range(3): #0,1,2
#     print(i)

# for i in range(1,5+1):
#     print(i)
# print("-"*60)

# for i in range(1,11,2):
#     print(i)
