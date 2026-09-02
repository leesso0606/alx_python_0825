# 응용문

alist=list(range(1,26))

alist2=[]
#리스트 안에 리스트
for i in range(0,26,5):
    alist2.append(alist[i:i+5])


# 출력하는 것뿐.
for i in range(len(alist)):
    if(i+1)%5!=0: #5개씩
        print(alist[i],end="") #옆으로 이동.
        alist2.append(i)
    else:
        print(alist[i])

        




# # 2. 1-25까지 리스트를 작성하고
# # 랜덤으로 리스트를 섞은 다음, 5개씩 2차원리스트를 만드시오

# import random
# alist=list(range(1,26))
# random.shuffle(alist)
# alist2=[]

# for i in range(0,len(alist),5):
#     alist2.append(alist[i:i+5])
# print(alist2)





# # 1. 문자열을 3자리씩 끊어서 리스트로 저장하시오
# aa="abcdefabcdefabcdefabcdefabcdef" #30개 / 문자열도 주석과 같다.
# print(len(aa))
# aa2=[]
# for i in range(0,31,3):
#     aa2.append(aa[i:i+3])

# print(aa2)



# -----------------------------------------------------------

# 1차원리스트를 2차원형태로 구성

# arr=[1,2,3,4,5,6,7,8,9] #len(arr)=9
# arr2=[]
# for i in range(0,len(arr),3):
#     arr2.append(arr[i:i+3])

# print(arr2)

# # 2차원으로 변경하고 싶음
# # arr2=[[1,2,3],
# #     [4,5,6],
# #     [7,8,9]
# #     ]