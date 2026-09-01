

stu_list=[
    [1,"홍길동",100,90,80,270,90.0],
    [2,"유관순",90,80,70,240,80.0],
    [3,"이순신",80,70,60,210,70.0]
]

while True:
    name = input("검색이름 입력:")
    flag = 0 # 초기화
    for i, stu in enumerate(stu_list):

        if name in stu:
            stu_index=stu.index(name)
            print("있음")
            flag = 1
            break

    if flag==0:
        print("해당하는 이름이 없습니다.")








# ---------------------------------------------------


# name_arr=["홍길동","유관순,","이순신","강감찬","김구"]

# name=input("검색할 이름을 입력하세요.>>")
# print(name_arr.index(name)) #바로쓰면 리스트에 없는 경우 에러뜸.
# print(name_arr.find(name)) #문자 find, rfind



# while True:
#     name=input("검색할 이름을 입력하세요.>>")
#     if name in name_arr:
#         no=name_arr.index(name) #리스트 주소 검색
#         print(no,":",name,"학생이 검색되었습니다.")

#         change=input("변경할 이름을 입력하세요.>>")
#         name_arr[no] = change
#         print(name_arr) #변경된 이름 확인

#     else:
#         print(name,"학생은 없습니다.")










# ------------------------------------------


# stu_list=[
#     [1,"홍길동",100,90,80,270,90.0],
#     [2,"유관순",90,80,70,240,80.0],
#     [3,"이순신",80,70,60,210,70.0]
# ]

# # 유관순-국어 100,영어 50으로 변경
# stu_list[1][2]=100
# stu_list[1][3]=50
# stu_list[1][5]=stu_list[1][2]+stu_list[1][3]+stu_list[1][4]
# stu_list[1][6]=stu_list[1][5]/3
# print(stu_list)
# [2, '유관순', 100, 50, 70, 220, 73.33333333333333] 로 변경됨.





# stu_list[0][1]="홍길자"로 변경
# print(stu_list)

# print(stu_list[0][2],stu_list[0][3],stu_list[0][4])





# --------------------------------------------------------




# aa=[]
# bb=[]
# value=0
# for i in range(0,100):
#     aa.append(value)
#     value+=2
# print(aa)

# for i in range(0,100):
#     bb.append(aa[99-i])
# print(bb)

# cc=list(range(0,200,2))
# print(cc)

# # 리스트내포
# dd=[i+2 for i in range(-2,198,2)]
# print(dd)

# a=list(range(0,10))
# print(a)

# --------------------------------------------

# aa=[10,20,30,40,50]
# bb=[1,2,3,4,5]

# print(aa*3)
# print(aa+bb) # aa와 bb가 값이 변경이 안됨. /  extend와 비슷

# aa.extend(bb) #aa의 값이 변경됨.
# print(aa)

# aa.append(0) # aa값이 변경
# # append, insert등



# ---------------------------------------

a=[1,2,3,4,5]
print(a[::-1]) # [5, 4, 3, 2, 1] /  역순
print(a[:3]) # [1, 2, 3] / 처음부터 2주소까지
print(a[3:]) # [4, 5] / 3주소부터 끝까지

aa=[1,2,3]
aa[1:2]=[10,20] # 주소 1에 2개를 넣는다. / [1, 10, 20, 3]
print(aa)



