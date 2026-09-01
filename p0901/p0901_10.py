
# # 숫자형-정수타입, 실수타입, 문자열타입, 불타입
# # 리스트, 튜플, 딕셔너리
# aa=[1,2,3,4,5] # 리스트 -수정, 추가 가능 aa[0]
# aa2=(1,2,3,4,5) #튜플- 수정,추가이 안됨. aa2[0]
# aa3={"key":"value",}  #딕셔너리




n_shape=["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
num=[1,2,3,4,5,6,7,8,9,10,11,12,13]
shape = ["SPADE","HEART","DIAMOND","CLOVER"]

# # 아래와 같이 출력하시오

# for s in shape:
#     for n in num:

#         print("{},{}".format(s,n_shape[n-1]))
    

# # SPADE,1
# # SPADE,2.....
# # ..
# # CLOVER,13 까지 출력


#  [["SPADE",1],["SPADE",2]..]형식으로
import random
card=[]
# card의 리스트 52개를 생성하시오
# 아래와 같이 출력하시오

for s in shape:
    for n in num:
        card.append([s,n])

random.shuffle(card)
print(card)