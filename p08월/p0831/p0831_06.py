





# 입력한 숫자를 모두 저장해서 프로그램을 종료할 때 출력하시오
noArr=[10,40,2,9,5]
no=[]
answer=[]
count=0
while True:
    i_no = int(input("숫자입력:"))
    # 0을 입력할 때 반복문 종료
    if i_no==0:break
    # 입력한 숫자 리스트에 저장
    no.append(i_no)

# noArr와 개수가 같은 
for i in no:
    if i in noArr:
        count = count+1
        answer.append(i)
    

# 반복문 종료할 때 입력된 숫자 모두 출력
print("리스트:",noArr)
print("입력 숫자:",no)
print("정답숫자:",answer)
print("프로그램 종료")





# ---------------------------------------


# ranNo=[1,5,9,7,4]
# inputNo=[1,2,3,4]
# answerNo=[]

# # 입력한 숫자와 랜던 숫자와 몇개가 맞는지 개수를 출력하시오.
# count=0
# for i in inputNo:
#     if i in ranNo:
#         count = count+1
#         answerNo.append(i)
#         print("있음")
#     else:
#         print("없음")

# print("개수:",count)