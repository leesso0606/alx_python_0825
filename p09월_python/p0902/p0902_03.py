
# isdigit() : 문자열이 숫자인지 확인/ isalpha():문자열이 문자(영어) / isalnum():문자열이 문자 또는 숫자로
# while True:

#     a=int(input("숫자를 입력하세요."))
#     if a.isdigit():
#         a=int(a)
#         break
#     else:
#         print("숫자가 아닙니다. 다시 입력하세요.")
#     print(a)







# ----------------------------------------------------


# split 분리, *전개연산자

# 
# 
str = input("날짜를 입력하세요.(2026/09/02)")
# 2026년9월2일로 작성
str2=str.split("/")
print(str2) # ['2026', '09', '02']
print("{}년{}월{}일".format(*str2))




# ---------------------------------------------


# # map,join ->문자열
# stu=[1,"홍길동",100,100,100]
# stu= list(map(str,stu)) #map 특정한 함수로 반복해줌.
# #  , 를 구분하여 문자열로 저장하시오
# stu2=",".join(stu)
# print(stu2)


# ------------------------------------------------------



# # map(함수, 반복리스트)
# aa=['1','2','3']
# print(map(int,aa)) #->map타입
# print(list(map(int,aa))) #->리스트타입





# ------------------------------------------------




# str=input("번호 3개를 입력하세요.(123/5/23)>>")
# # 3개의 합을 구해서 출력하시오.


# str_list=str.split("/") #/로 분리해도 문자열 타입
# str_list=list(map(int,str)) # 맵->리스트타입으로 변경 그러면 int(s)를 s로 변경가능.
# sum=0
# for s in str_list:
#     sum=sum+int(s) #정수타입으로 변환.
# print(sum)