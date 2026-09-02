
alist=list(range(1,21))
nlist=[]

# for문 사용
for a in alist:
    if a%3==0:
        nlist.append(a)
print(nlist)

# 위와 같은 결과 /  파이썬에서만 사용가능 / 리스트내포:컴프리핸션
a=[n for n in range(1,21) if n%3==0]
print(a)








# ---------------------------------------------------



# # 리스트 자동생성방법 4가지
# alist=[i for i in range(1,11)] #리스트 내포:컴프리핸션
# alist2=list(range(1,11))
# alist3=[0]*10
# alist4=[0,0,0,0,0,0,0,0,0,0]



# ----------------------------------


# engs = {
#     "car":"자동차",
#     "color":"색상",
#     "pig":"돼지",
#     "love":"사랑",
#     "phone":"전화기"
# }


# for k,v in engs.items(): #(키:값)이 나오는데 k에 키값, v에 값을 넣는것.
#     print(k,"는 한국어로 무엇일까요?")
#     answer=input("정답:")
#     if answer==v:
#         print("정답입니다.")
#     else:
#         print("오답입니다.")





# ---------------------------------------------------------

name_dic = {
    "aaa":'토마토',"ddd":"바나나","eee":"딸기","bbb":"배"
}

# [b,c,a,k,l,d,z,y]


import operator
name_sort1 = []
# name_sort1 = sorted(name_dic.items(),key=operator.itemgetter(0))
# name_sort1 = sorted(name_dic.items(),key=lambda x:x[0]) #x[0]:aaa/ sorted:순차정렬->시간이 오래걸려서 정렬은 안하는 편
name_sort1 = sorted(name_dic.items(),key=lambda x:x[0],reverse=True) # 역순

print(name_sort1)





#---------------------------------- 


# stu={"no":1,"name":"홍길동","total":100}

# for i,v in stu.items():
#     print(i,":",v)



# -------------------------------------------------------------------------------------------------

# stu={"no":1,"name":"홍길동","total":100}

# print(stu.keys()) #모든 키값만
# print(stu.values()) #value값만
# print(stu.items()) # 둘다 나온다

# # 딕셔너리리스트->list()타입으로 변환
# s_list=list(stu.values())
# print(s_list)



# ---------------------------------------------------------------


# # 딕셔너리 : {"key":"value",} 
# stu={"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"music":100}
# # 리스트  stu_arr=[1,"홍길동",100,100,100,100]

# print(stu)

# # 딕셔너리 추가: 없는 키값 입력하면 출력됨.
# stu["total"]=400
# stu["avg"]=stu["total"]/4
# print(stu)

# # 딕셔너리 수정: 있는 키값에 값을 넣으면 수정됨.
# stu["kor"]=50
# print(stu)

# # 딕셔너리 출력: 키 출력
# print(stu["kor"])

# # 딕셔너리 삭제 : del(키)
# del(stu["eng"])
# print(stu)

# stu_list=[
#     {"no":1,"name":"홍길동","kor":100,"eng":100,"math":100,"total":300,"avg":100},
#     {"no":2,"name":"유관순","kor":100,"eng":100,"math":100,"total":300,"avg":100},
#     {"no":3,"name":"이순신","kor":100,"eng":100,"math":100,"total":300,"avg":100}
# ]
# # 있는키 입력 :수정
# stu_list[0]["name"]="홍길자"
# # 출력
# print(stu_list[0]['name'])
# print(stu_list[0]['kor'])
# # 추가
# stu_list[0]['rank']=1
# # 삭제
# del(stu_list[0]['no'])
# print(stu_list)
# 특정값만 출력.
# print(stu_list[0].get('no'))

