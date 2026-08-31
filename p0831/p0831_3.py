a_list=["딸기","바나나","사과"]
# 0:"딸기"
# 1:"바나나"
# 2:"사과"
# enumerate : 번호, 값 2개가 동시에 전달 됨.
for i,v in enumerate(a_list):
    print("{}:{}".format(i,v))