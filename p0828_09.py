# # 예시로 번호표 를 표현할 때
# for i in range(1,10):
#     for j in range(0,10):
#         for k in range(0,10):
#             print("{}{}{}".format(i,j,k))


# -------------------------------
# for i in range(1,4):
#     for j in range(1,4):
#         for k in range(0,10):
#             print(i,j,k)
# print(f"{i} x {j} = {i*j}")


# ------------------------------------
#  두 수식 같은 말. 구구단으로 응용가능
# #for i in range(1,10):
#     print("2 X {} = {}".format(i,i*2))
# # for i in range(1,10):
# #     print(f"2 X {i} = {2*i}")


# ------------------------------------------
# sum=0
# for i in range(1,14):
#     sum=sum+i
# print("합계: ",sum)

# # sum이 100 넘어가는 시점은 i가 얼마일때?

# sum=0
# for i in range(1,10):
#     sum=sum+i
#     if sum>11:
#         print("10보다 크기 바로 앞일때:",i-1)
#         print("10초과 전 일 때 시점: ",sum-i)
#         break

stu=[]
for i in range(3):
    print(i+1,"번째")
    no=i+1
    name=input("이름 입력: ")
    kro=int(input("국어점수 : "))
    stu.append([no,name,kor])

for i in range(3):
    print("{}번\t이름:{} \t{}점".format(no,name,kro))

print("{}번\t이름:{} \t{}점".format(no,name,kro))
# print(f"{no}\t{name}\t{kro}")

# #  and를 넣으면 옆쪽으로 출력된다.
# print("1",end="\t")
# print("2",end="\t")
# print("3",end="\t")




# -----------------------------------------

# # i 든 _ 든 똑같은 변수임
# for i in range(10):
#     print("안녕")
# for _ in range(10):
#     print("안녕")



# ------------------------------------------


# #  for 변수 in 범위 : 범위만큼 반복
# for i in range(5): #i에 5번 반복한다.
#     print(i)

# for i in range(5): #i에 5번 곱한값을 반복한다.
#     print(i*10)

# for i in range(0,10,2): # 0-9까지 2간격
#     print(i)

# for i in [1,5,3,2]:
#     print(i)

# for i in "안녕하세요":
#     print(i)

# arr=list(range(1,11))
# print(arr)