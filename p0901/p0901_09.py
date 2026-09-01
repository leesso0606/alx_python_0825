
# a_list=["딸기","바나나","사과"]
# # 0:"딸기"
# # 1:"바나나"
# # 2:"사과"

# # enumerate : 번호, 값 2개가 동시에 전달 됨.
# for i,v in enumerate(a_list):
#     print("{}:{}".format(i,v))

# 빙고게임 만들기
import random
a_arr=list(range(1,26))
random.shuffle(a_arr)

while True:

    print(" "*15,end="") # end="" 옆으로 출력된다.
    print(" [ 빙고게임 ] ")
    print("-"*60)
    # 5x5형태로 만들기.
    for i ,v in enumerate(a_arr):
        if (i+1)%5!=0:
            print(v,end="\t")
        else:
            print(v)
    print("-"*50)

    num=int(input("원하는 번호를 입력하세요>>"))
    # 작성한 번호를 X로 변경
    if num in a_arr:
        index=a_arr.index(num)
        a_arr[index]="X"










# ---------------------------------------------------



# aa = list(range(1,13))
# print(aa) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# a_arr=[]

# for i in range(0,12,4):
#     a_arr.append(aa[i:i+4])
# print(a_arr)

# # [
# #     [1,2,3,4],
# #     [5,6,7,8],
# #     [9,10,11,12]
# # ]


# # --------------------

# import random
# aa=list(range(1,26))
# random.shuffle(aa)

# for i,v in enumerate(aa):
#     if i==0: 
#         print(v,end="\t")
#         continue
#     if (i+1)%5!=0:
#         print(v,end="\t")
#     else:
#         print(v)



# -----------------------------------------------


# a_arr=[1,5,10,20,90,100,7,2]
# a_arr2=[*a_arr] #깊은 복사 /  새로 만드는것
# a_arr3=a_arr.copy() # 깊은 복사
# a_arr[0]=100

# a_arr.sort() # 정렬하면 리스트 못돌림./ 다시하고 싶으면 리스트 다시 만들어야함.
# a_arr.sort(reverse=True)
# a_arr.reverse # 같은 말

# print(a_arr)
# print(a_arr2)
# print(a_arr3)

# # 삭제
# a_arr.pop() # 맨 뒤 주소 삭제.
# print(a_arr)