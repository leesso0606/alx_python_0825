# # 반복문을 사용하여 1-100까지 합을 출력하시오.
# sum=0
# for i in range(1,101):
#     sum=sum+i
# print("합계:",sum )


# 200을 넘는 시점의 i의 값과 i번째 합계를 출력하시오
sum1=0
for i in range(1,101):
    sum1=sum1+i
    if sum1>200:
        print("200이 넘을 때 i: ",i)
        print("i번째 합계:",sum1 )
        break


# 200을 넘는 이전 시점의 i와 합계를 출력하시오
sum2=0
for b in range(1,50):
    sum2=sum2+b
    if sum2>200:
        print("200이 넘기전 i:",b-1)
        print("200이 넘기 전 i번째의 합:",sum2-b)
        break


# # 구구단을 출력하시오.
# for c in range(1,10):
#     for d in range(1,10):
#         # print("{} X {} = {}".format(c,d,c*d))
#         print(f"{c} X {d} = {c*d}")


# # 여러명의 학생 성적을 출력할 때
# # 리스트일때만 반복문을 쓸 수 있다.
name=[]
kor=[]
# for _ in range(2):
#     name.append(input("이름:"))
#     kor.append(int(input("국어점수:")))
# # 리스트에 
stu=[] #추가
for n in range(2):
    name=input("이름:")
    kor=int(input("국어점수:"))
    stu.append([name,kor]) #으로 쓸수도 있다.

# for n in range(2):
for n in stu:
    print("{}\t{}".format(n[0],n[1]))

# # 변수가 일일이 지정되어 있으면 반복문 사용 불가능
# # print("{}\t{}".format(name1,kor2))
# # print("{}\t{}".format(name2,kor2))
# # print("{}\t{}".format(name3,kor3))
