

# [학생성적]
# 홍길동 70
# 유관순 100
# 이순신 90을 출력하시오

# name = []
# kor = []
# eng = []
# for i in range(3):
#     name.append(input("이름입력 :"))
#     kor.append(int(input("국어점수입력 : ")))

# print("[ 학생성적 ]")
# for i in range(len(name)):
#     print(f"{name[i]}\t{kor[i]}")

#  영어, 수학, 합계, 평균을 추가할 경우
name=[]
kor=[]
eng=[]
math=[]
total=[]
avg=[]
for i in range(3):
    name.append(input("이름:"))
    k_input=int(input("국어점수:"))
    kor.append(k_input)
    e_input=int(input("영어점수:"))
    eng.append(e_input)
    m_input=int(input("수학점수:"))
    math.append(m_input)
    total.append(k_input+e_input+m_input)
    avg.append((k_input+e_input+m_input)/3)

print("[학생 성적]")
print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
print("-"*60)

for i in range(len(name)):
    print("{}\t{}\t{}\t{}\t{}\t{}\t{:2f}".format(i+1,name[i],kor[i],eng[i],math[i],total[i],avg[i]))
    # print(f"{i+1}\t{name[i]}\t{kor[i]}\t{eng[i]}\t{math[i]}\t{total[i]}\t{avg[i]:2f}")










# --------------------------------

# list_a=["바나나","딸기","사과"]
# # 1:바나나,2:딸기,3.사과 처럼 나오게 하려면
# j=1
# for i in list_a:
#     print(j,":",i)
#     j=j+1


# # 리스트에 번호가 필요하면 enumerate 사용
# for i, value in enumerate(list_a): #index번호 리스트값 2개
#     print(i+1,":",value)

# for i in range(3):
#     print(i+1,list_a[i])

# for i in range(len(list_a)):
#     print(i+1,":",list_a[i])


# for i in range(1,4):
#     print(i)






# -------------------------

# list_a=["바나나","딸기","사과"]
# # 과일입력을 3번 추가하려면
# for i in range(3):
#     list_a.append(input("과일입력:"))
# for i in list_a:
#     print(i)



# ----------------------------


# # 구구단을 출력하시오


# # for i in range(2,10):
# #     for j in range(1,10):
# #         print("{}X{}={}".format(i,j,i*j))


# # 5를 입력을 받아 5단부터 출력하시오.
# a=int(input("시작되는 단을 입력하시오"))
# b=int(input("끝이되는 단을 입력하시오"))

# for i in range(a,10):
#     for j in range(1,b+1):
#         print("{}X{}={}".format(i,j,i*j))


# # 5단만 출력

# for i in range(a,a+1):
#     for j in range(1,b+1):
#         print(f"{i}X{j}={i*j}")


# -----------------------------------

# sum=0
# # 입력한 첫번째 숫자부터 두번째 입력한 숫자까지 합을 구하시오
# # 2,5
# # 그대로 실행 시킬때 a가 b보다 작으면 합계가0으로 나옴
# # 하지만 if문을 사용하여 값 치환

# a=int(input("첫번째 숫자:"))
# b=int(input("두번째 숫자:"))
# c=0
# if a>b:#a가 b보다 클때만.
#     a,b=b,a
#     # c=a
#     # a=b
#     # b=c /  a,b=b,a와 같은말

# for i in range(a,b+1):
#     sum=sum+i
# print("합계:",sum)



# ------------------------------------


# # 3개의 입력한 숫자의 합을 구하시오.
# # 1. 입력 int(input("숫자입력:"))
# # 2. for문 3번 
# # 3. sum

# sum=0
# no1=[]
# for i in range(3):
#     no=int(input("숫자를 입력하시오.")) # 이 조건을 for문에 합해 반복하도록 넣으것
#     no1.append(no)
#     sum=sum+no
    
# print("입력한 숫자의 합:",sum)
# print("입력값:",no1)





# --------------------------

# # 1-100까지 합을 출력하시오
# sum=0
# for i in range(1,101):
#     sum=sum+i
# print("합:",sum)

# # 홀수의 합을 구하시오
# for i in range(1,101,2):
#     sum+i
# print("합:",sum)

# #  7의배수 합을 구하시오
# for i in range(1,101):
#     if i%7==0:
#         sum=sum+i
# print("합:",sum)






# ------------------------


# # 합계:55
# sum=0
# for i in range(1,11):
#     sum=sum+i
# print("합계:",sum)

# # 1-10 까지 곱
# result=1
# for i in range(1,11):
#     result=result*i
# print("곱:",result)
# print("곱:{:,}".format(result))


# ------------------------------


# 합계가 100이 넘을 때 i는?
# sum=0
# for i in range(1,30):
#     sum=sum+i
#     if sum>100:
#         print(i,":",sum)
#         break #for 문을 강제종료


# no=0
# sum=0
# sum2=0
# for i in range(1,30):
#     sum=sum+i
#     if sum>100:
#         print(i,":",sum)
#         break #for 문을 강제종료
# print("합계가 100을 넘을 때 i의 갑:",no)
# print("그때의 합계:",sum2)
# print("합계가 100을 넘기전 i의 값:",no-1)
# print("그때의 함계:",sum2-no)








# ----------------------------------------------------------


# # 구구단을 아래로 출력하시오.

# for i in range(2,10):
#     print(f"[{i}단]",end="\t")
# print()
# for i in range(1,10):
#     for j in range(2,10):
#         print(f"{j}X{i}={i*j}",end="\t")
#         # print("{}x{}={}".format(i,j,i*j),end="\t")
#     print() #공백을 생기게 해줌.
    