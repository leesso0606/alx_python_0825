fruit=["사과","수박","딸기","참외","복숭아"] #숫자 0부터 시작
print(fruit[2]) # 딸기
print(fruit[1:4]) # 1,2,3번까지 출력, 뒷 숫자 전까지 출력/ 수박, 딸기,참외
print(fruit[2:]) # 2번부터 끝까지 출력/ 딸기, 참외, 복숭아
print(fruit[:3]) # 처음부터 3번 앞에까지 출력 / 사과, 수박, 딸기
print(fruit[:]) # 모두 출력/ 사과, 수박, 딸기,참외,복숭아
print(fruit[::2]) # 처음부터 끝까지 2간격 마다 출력 / 사과, 딸기, 복숭아
# [:]는 슬라이싱이라고 말함.
arr=[1,2,3,4,5,6,7,8,9]
print(arr[::2]) # 홀수만 나옴
print(arr[1::2]) # 짝수만 나옴
print(arr[0],arr[2]) # 각각 지정해 줘야 출력됨 / 1,3






# import random
# r_num=random.randint(1,10)
# # 3개 숫자입력
# arr=[]
# # 리스트에 값을 추가할 시 append사용
# arr.append(int(input("1.1-10 숫자입력:")))
# arr.append(int(input("2.1-10 숫자입력:")))
# arr.append(int(input("3.1-10 숫자입력:")))
# # 첫번째 방법
# if r_num in arr:
#     print("당첨")
# else:
#     print("꽝")
# print("랜덤숫자:",r_num)
# print("입력숫자:",arr)

# # 두번째 방법
# if r_num in arr: print("당첨")
# else: print("꽝")

# # 세번째 방법
# print ("당첨") if r_num in arr else print("꽝")






# 비교시 리스트는 ("검색내용" in 리스트) 하면됨.
# a="사과"
# b="딸기"
# c="수박"
# d="참외"
# e="복숭아"

# # a,b,c,d,e 중 참외가 있는지 확인하고, 있으면 참외가 있습니다. 없으면 참외가 없습니다.
# if a=="참외"or b=="참외"or c=="참외"or d=="참외"or e=="참외":
#     print("참외가 있습니다.")
# else:
#     print("참외가 없습니다.")

# # 리스트
# fruit=["사과","수박","딸기","참외","복숭아"]
# if "참외" in fruit: # in이라는 명령어를 사용하여 여부 확인가능.
#     print("참외가 있습니다.")
# else:
#     print("참외가 없습니다.")




# # 1-10 사이의 숫자 3개를 입력받아
# # 랜덤숫자를 맞추면 당첨, 그렇지 않으면 꽝

# # 반복문을 사용할 수 없음
# # 일반 변수는 반복문을 사용하기 힘듬. 하지만 리스트는 반복문 가능.
# no1=int(input("1.숫자입력:"))
# no2=int(input("2.숫자입력:"))
# no3=int(input("3.숫자입력:"))
# print("입력숫자:",no1,no2,no3)

# num=[0,0,0]
# num[0]=int(input("1.숫자입력:"))
# num[1]=int(input("2.숫자입력:"))
# num[2]=int(input("3.숫자입력:"))
# print("입력숫자:",num)



# # 리스트 추가 가능 타입: 모든 타입
# arr = [1,"안녕",1.2,True,[1,2,3]]
# print(arr[1]) # 안녕
# print(arr[3]) # True
# print(arr[4][1]) # 2
# a=arr[4]
# print(a[2]) #3




# # 리스트 = 배열
# a=1
# arr=[1,2,3,4,5]
# print(type(a))  # int
# print(a) # 1
# print(a+1) #2
# print(type(arr)) #last
# print(arr) #[1,2,3,4,5]
# print(arr[4]+1) # 주소는 0번부터. 0번째-4번째 숫자, 5+1=6이 나옴.
# #print(arr+1)-> 에러
# print(len(arr)) #리스트 개수 Iength줄임.
# # 리스트는 []시작
# # 리스트는 여러개 저장
# # 리스트는 0부터 주소가 시작
# # 리스트는 print하면 모두 출력가능
# # 리스트의 특정주소로 그 값을 출력할 수 있음
# # 리스트 개수 : len()
# # 리스트 안에는 모든 타입을 넣을 수 있음 - 정수, 실수, 물자열, 불, 리스트, 튜플, 딕셔너리

