

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

# 합계가 100이 넘을 때 i는?
sum=0
for i in range(1,30):
    sum=sum+i
    if sum>100:
        print(i,":",sum)
        break #for 문을 강제종료










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
    