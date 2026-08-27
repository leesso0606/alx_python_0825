score =65
# score 60점이상이면 합격,불합격
if score>60:print("합격")
else: print("불합격") # 명령어가 한줄일 때만 가능. 예로 print를 하라는게 2개면 불가능.

# if문 축약, 나중에 숙달되면 축약하여 적을 수 있음.
reuslt="합격" if score>=60 else "불합격"




# # 날짜 함수를 사용하려면
# import datetime

# now= datetime.datetime.now()

# # 해당월에 따라 봄, 여름, 가을, 겨울이라고 출력하시오
# # 겨울12,1,2 봄3,4,5 여름6,7,8 가을9,10,11
# # 비교문을 사용해서
# # 해당월 계절을 출력하시오

# month=now.month
# month=int(input("월을 입력하세요."))
# if 11>=month>=9:
#     print("가을")
# elif 8>=month>=6:
#     print("여름")
# elif 5>=month>=3:
#     print("봄")
# else:
#     print("겨울")


# if month==12 or 2>=month>=1:
#     print("겨울")
# elif 8>=month>=6:
#     print("여름")
# elif 5>=month>=3:
#     print("봄")
# else:
#     print("가을")






# # if :조건문
# # if
# # if-else
# # if elif else
# # if elif elif else

# # if 조건문:
# #    들여쓰기 되어야 함.
# # else:
# #    들여쓰기 되어야 함.

# if 10>5:
#     pass # 출력이나 기타 프로그램이 없을시 pass
# print("프로그램")

# if 10>5: pass
# if 10>5: print("참") # if 한줄로 가능
# if 10>5:
#     print("참")

# if 10>5: # 명령어가 2줄이상이면 다음줄에 넣어야 함.
#     print("참")
#     print("좋아요")




# # 랜덤점수를 생성해서 
# import random
# # 90점이상은 A, 80점이상은 B, 70-C, 60-D, 나머지 
# # 90-92점 A-, 93-97 A, 98 A+
# # 80-82점 B-, 83-87 B, 88 B+
# # 70-72점 C-, 73-77 C, 78 C+
# # 랜덤점수 출력하시오
# score=random.randint(0,100)
# print("점수:",score)

# if score>=90:
#     if score>=99:
#         print("A+")
#     elif score>=93:
#         print("A")
#     else:
#         print("A-")
# elif score>=80:
#     if score>=89:
#         print("B+")
#     elif score>=83:
#         print("B")
#     else:
#         print("B-")
# elif score>=70:
#     if score>=79:
#         print("C+")
#     elif score>=73:
#         print("C")
#     else:
#         print("C-")
# elif score>=60:
#     if score>69:
#         print("D+")
#     elif score>=63:
#         print("D")
#     else:
#         print("D-")
# else:
#     print("F") # 선생님이 하신것.



# if score>=98:
#     print("A+")
# elif score>=93:
#     print("A")
# elif score>=90:
#     print("A-")
# elif score>=88:
#     print("B+")
# elif score>=83:
#     print("B")
# elif score>=80:
#     print("B-")
# elif score>=78:
#     print("C+")
# elif score>=73:
#     print("C")
# elif score>=70:
#     print("C-")
# elif score>=60:
#     print("D")
# else:
#     print("F")  이건 내가 한것. 시간이 오래걸림..

















# import random
# # 0-100점 랜덤숫자 생성
# # 60점 이상은 합격,
# # 50-59점 까지는 재시험 -> if 또는elif radom_score>=50: / elif 59>=random_sore>=50:->같은말이지만 후자가 조건많아서 느림.
# # 0-49점 까지는 불합격으로 출력하시오
# random_score=random.randint(0,100)
# if random_score>=60:
#     print("합격")
# elif random_score>=50: # 자바의 경우 elif (59>=score) and (50<=score):
#     print("재시험")
# else:
#     print("불합격")
# print("랜덤점수:",random_score)



# import random
# random_no = random.randint(-2,2)
# print("랜덤숫자:",random_no)

# # 랜덤숫자가 양수인지 음수인지 출력하시오
# if random_no>0:
#     print("양수")
# elif random_no==0:
#     print("0") #엘리프
# else:
#     print("음수") #엘스



# # 조건문을 여러개
# score=65
# if score>=90:
#     print("A")
# elif score>=80:
#     print("B")
# elif score>=70:
#     print("C")
# elif score>=60:
#     print("D")
# else:
#     print("F")



# 조건문안에 조건문
# a=1
# if a>50:
#     if a<100:
#         print("50보다 크고 100보다 작은수")
#     else:
#         print("50보다 크고 100보다 큰수")
# else:
#     print("50보다 작은수")
# if안에 if문을 쓸 수 있지만3번이상은 권장하지 않음