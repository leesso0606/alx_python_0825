# 원하는 값 in 리스트, 원하는 값 not-in리스트

arr=[1,3,5,7,9]
if 6 in arr:
    print("원하는 수가 있습니다.")
else:
    print("원하는 수가 없습니다.")





# # 정렬 순차정렬: 리스트명.sort(), 역순정렬: 리스트명.sort(reverse=True)
# arr=[1,5,8,3,2] #리스트
# arr.sort()
# print(arr) #[1, 2, 3, 5, 8]
# arr.sort(reverse=TimeoutError)
# print(arr) # [8, 5, 3, 2, 1]




# # 리스트 삭제 - del, pop(), remove, clear(모두삭제)
# arr=[1,2,3,4,5,True,"안녕"]
# print(arr) #[1, 2, 3, 4, 5, True, '안녕']
# # 리스트명.pop()
# arr.pop(2) # 2번주소 삭제
# print(arr) #[1, 2, 4, 5, True, '안녕']

# #del 리스트명 []
# del arr[0] # 0번째 삭제 / del 리스트명[]
# print(arr) #[2, 4, 5, True, '안녕']

# # 리스트명.remove()
# arr.remove("안녕")
# print(arr) #[2, 4, 5, True]
# # 리스트명.clear() -> 전부삭제
# arr.clear()
# print(arr) #[]











# # 리스트 추가
# a=[1,2,3]
# b=[4,5,6]
# #원본에 영향이 없음
# print(a+b)
# print(a)
# # 원본에 영향이 있음 
# a.extend(b)
# print(a) # [1, 2, 3, 4, 5, 6] a원본은 값을 직접 변경해서 추가해줌.
# print(b)






# # 리스트 추가 :append, insert
# # append는 뒤에추가
# arr=[1,2]
# arr.append(3)
# arr.append(9)
# arr.append(5)
# print(arr)
# # [1, 2, 3, 9, 5]
# # insert : 원하는 위치에 추가 / 어지간하면 사용안함. 데이터가 많을 수록 오래걸림.
# arr.insert (1,20)
# print(arr) #[1, 20, 2, 3, 9, 5]





# arr1=[1,2,3]
# arr2=[4,5]
# arr3=arr1+arr2 # 리스트+리스트=리스트 /리스트끼리 합쳐짐
# print(arr1+arr2)
# print(arr3)

# arr4=arr1*3
# print(arr4) # 반복됨.

# aaa=[0,0,0,0,0,0,0,0,0,0]
# aaa2=[0]*10 # 둘 같은말
# print(aaa)
# print(aaa2)
# print(aaa==aaa2)







# arr=[[1,2,3],[4,5,6],[7,8,9]]
# arr=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ] # 둘 동일한 말. 리스트는 \는 안 넣어도됨.
# print(arr[1]) # [4,5,6]
# print(arr[1][1]) # 5



# # 문자열-리스트형대로 저장가능.
# name="안녕하세요반갑습니다"
# print(name) #안녕하세요반갑습니다
# print(name[1]) #녕
# print(name[6]) #갑
# print(name[5:8]) #반갑습
# print(name[::2]) #안하요갑니
# if "하" in name:
#     print("있습니다.")
# else:
#     print("없습니다.") #있습니다.





# fruit=["사과","수박","딸기","참외","복숭아"] #숫자 0부터 시작
# print(fruit[2]) # 딸기
# print(fruit[1:4]) # 1,2,3번까지 출력, 뒷 숫자 전까지 출력/ 수박, 딸기,참외
# print(fruit[2:]) # 2번부터 끝까지 출력/ 딸기, 참외, 복숭아
# print(fruit[:3]) # 처음부터 3번 앞에까지 출력 / 사과, 수박, 딸기
# print(fruit[:]) # 모두 출력/ 사과, 수박, 딸기,참외,복숭아
# print(fruit[::2]) # 처음부터 끝까지 2간격 마다 출력 / 사과, 딸기, 복숭아
# # 슬라이싱이라고 말함. [시작:끝:간격] 간격은 없어도 상관없음.
# arr=[1,2,3,4,5,6,7,8,9]
# print(arr[::2]) # 홀수만 나옴
# print(arr[1::2]) # 짝수만 나옴
# print(arr[:-1]) #뒤부터는 -1부터 시작, 마지막 제외
# print(arr[::-1]) #거꾸로 출력, 리스트 역순정렬
# print(arr[0],arr[2]) # 각각 지정해 줘야 출력됨 / 1,3






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

