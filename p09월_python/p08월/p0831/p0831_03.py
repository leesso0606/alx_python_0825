

# 리스트 개수 늘리는 방법.
alist=[]
print(len(alist))
alist2=[0,0,0] #3개
print(len(alist2))
alist3=[0]*10
print(len(alist3))
alist4=list(range(10)) #0,1,2,.... 0부터 시작
print(alist4)
alist5=[i+5 for i in range(10)] #리스트 내포/ 새롭게 계산식을 더해서 다른수부터 시작도 가능/ i+5->i*i 등 다른 수로 가능. 
print(alist5)


# ----------------------------------------


# for i in range(10): # for문에 들어올 수 있는 것.range91,11,2)/ [리스트]/ 문자열
#     print(i)


# -----------------------------------


# a_list=["딸기","바나나","사과"]
# # 0:"딸기"
# # 1:"바나나"
# # 2:"사과"

# # enumerate : 번호, 값 2개가 동시에 전달 됨.
# for i,v in enumerate(a_list):
#     print("{}:{}".format(i,v))