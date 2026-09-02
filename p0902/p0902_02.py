
### 앞뒤공백제거 - strip()
a="     abc    "
print(a.strip()) # 공백제거는 해줌. 하지만 a에 반영은 안됨.
print(a)

### 중간공백제거 - replace()
b="   a   b"
print(b.replace(" ","")) # " "을 ""로 교체해라

### 분리 - split ->리스트 타입으로 변환
c="딸기,수박,바나나,사과"
print(c.split(","))


# -->> 응용
d="1,홍길동,100,100,100,300,100.0" #문자열타입
dlist=d.split(",") # , 로 분리
dlist[2]=90
dlist[3]=int(dlist[3])
dlist[4]=int(dlist[4])
dlist[5]=dlist[2]+dlist[3]+dlist[4]
dlist[6]=dlist[5]/3
dlist2=[str(i)for i in dlist]
print(dlist)


# 특정 문자로 결합 -join
# 문자열 리스트만 변경가능. join결합
# 문자열로 변환됨.
d_str=",".join(dlist2)
print(d_str)


# 5. count:문자열안에 해당 문자가 몇개 있는지 확인
# 6. find: 문자열 안에 해당 문자 위치 반환, 없으면 -1
# 7. index: find와 동일 없으면 에러.



# -----------------------------------------------------



# # join : 추가를 해주는것.
# aa="/"
# bb=aa.join(["바나나","딸기"])
# print(bb) #바나나/딸기
# print(type(bb))



# ------------------------------------------------

# strip, replace : 

# ss="  파이썬" # strip : 공백삭제
# ss2="<<<<파<<이<썬" #replace(a,b) : a를 b로 대체시키는것.

# print(ss.strip())
# print(ss2.replace("<",""))



# 공백제거할 때 사용 -> 앞,뒤 공백 삭제
# aa= input("이름을 입력하세요.>> ").strip()

# aa=[1,2, 3, 4 ,5] 와 같이 공백이 있을 때



# ------------------------------------------------------



# #  리스트에서 찾을 때 : .find()/.index()

# ss="파이썬 공부!! 열심히 합시다. 파이썬"
# print(ss.count("공부"))
# print(ss.count("파이썬"))
# print(ss.find("공부")) # 4
# print(ss.find("자바")) # -1
# print(ss.index("자바")) # index 는 값이 없으면 에러



# -----------------------------------------


#  # split(a) : a를 분리
# aa="a/b/c/d/f/g"
# aa_list=aa.split("/") # 분리해서->리스트변환
# print(aa_list)

# bb="100,10,5,4,1"
# # 모든 수의 합을 구하시오. : 문자열->정수형으로 변경하여 합을 구해야함.
# bb_list=bb.split(",") # ,분리 
# print(bb)

# bb_list2=[int(i) for i in bb_list] # int 정수로 변경
# print(bb_list2)

# sum=0 #변수 지정
# for b in bb_list2:
#     sum=sum+b
# print(sum)



# -----------------------------------------------



# 문자를 딕셔너리 형태로 정리.


# aa = "가나다라가가가나나다라라라라라라라"
# ##
# # {가:10,나:5,다:11...} 딕셔너리형태로 만드시오
# print(aa.count("가"))
# aa_dic={}
# for a in aa:
#     if a in aa_dic:
#         aa_dic[a]=aa_dic[a]+1
#     else:
#         aa_dic[a]=1
# print(aa_dic)





# ----------------------------------------------------------




# a=[1,2,3,4,5]
# b=[10,20,30,40,50]
# c=[]


# # # zip : 두 리스트나 튜플을 짝지을 수 있다.
# c=list(zip(a,b)) 
# d=dict(zip(a,b)) 
# print(c) # [(1, 10), (2, 20), (3, 30), (4, 40), (5, 50)] ->리스트 형태.() 안에 있는 수정 불가능.
# print(d) # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50} -> 튜플형태.


# for i,j in zip(a,b):
#     c.append([i,j])
# print(c)

# for i in range(len(a)):
#     c.append([a[i],b[i]])
# print(c)







# -----------------------------------------------------------------

# 리스트 입력/생성 방법


# a1=[1,2,3,4,5]
# a2=[0]*5
# a3=list(range(1,6))
# a4=[i for i in range(1,6) if i%2==0] #리스트 내포
# print(a4)


# ---------------------------------------------------------------------


# # count:리스트 안에 원하는 값의 개수를 알수 있다.

# # aa=["바나나","딸기","사과","딸기","딸기","사과"]
# # print(aa.count("바나나"))
# # print(aa.count("사과"))
# # print(aa.count("딸기"))
# aa=[1,2,3,1,1,1,2,3,1,1,1,2,2,3]

# # 리스트 안에 중복되는 것 여부, 개수를 구할 때 사용됨.
# # a_dic={"바나나":1,"딸기":3,"사과":2}
# a_dic={1: 7, 2: 4, 3: 3}
# aa_dic={}
# for a in aa:
#     if a not in aa_dic: #없으니까 1
#         aa_dic[a]=1
#     else:
#         aa_dic[a]=aa_dic[a]+1 #있으면 개수 +1
#         print("있습니다.")

# print(aa_dic)







# # 딕셔너리
# a_dic={"바나나":1,"딸기":3,"사과":2}
# print(a_dic["바나나"])

# # 추가
# a_dic["배"]=5
# print(a_dic)

# # 삭제
# del a_dic["바나나"]
# print(a_dic)

# # 수정
# a_dic["사과"]=100
# print(a_dic)








# -----------------------------------------------


# a=10
# a2=0
# a=a2
# print(a2) #0
# a=100
# print(a2) #0


# ---------------------------------------------------------



# alist=[1,2,3]
# alist2=[]
# # alist2=alist #얕은 복사
# alist2 = [*alist] # 깊은복사
# print(alist2) #[1, 2, 3]

# alist[0] = 100 #  alist의 0번째 주소값을 100으로 변경
# print(alist) # [100, 2, 3]
# print(alist2) # [1, 2, 3]

