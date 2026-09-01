# 로또 맞추기 
# 학생성적 프로그램 만들기 외우기

# 학생성적입력-변수, 리스트, 리스트-딕셔너리,리스트-리스트
# 리스트 만드는법 - 직접입력, [0]*9,list(range(1,20))

# stu_list=[
#     [1,"홍길동",100,100,100,300,100.0],
#     [2,"유관순",100,100,100,300,100.0],
#     [3,"이순신",100,100,100,300,100.0]
# ]


stu_list=[]
# stu_list.append([1,"홍길동",100,100,100,300,100.0])
# stu_list.append([2,"유관순",100,100,100,300,100.0])
# stu_list.append([3,"이순신",100,100,100,300,100.0])


# for i in range(3): #무조건 (숫자)번 해야지 마무리됨
#     no=input("번호입력:")
#     name=input("이름입력:")
#     kor=int(input("국어입력:"))
#     eng=int(input("영어입력:"))
#     math=int(input("수학입력:"))
#     total=kor+eng+math
#     avg=total/3
#     stu_list.append([no,name,kor,eng,math,total,avg])

# print(stu_list)



while True: 
    no=len(stu_list)+1 
    # no=input("번호입력:")
    print("자동번호:",no)
    name=input("이름입력(종료하려면0):")
    if name=="0":break
    kor=int(input("국어입력:"))
    eng=int(input("영어입력:"))
    math=int(input("수학입력:"))
    total=kor+eng+math
    avg=total/3
    stu_list.append([no,name,kor,eng,math,total,avg])

print("입력한 학생성적:",len(stu_list))

print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
print("-"*60)
for s in stu_list:
    print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*s))




# -----------------------------------------------------


# # 리스트 만드는법 - 직접입력, [0]*9,list(range(1,20))
# # [1,2,3,4,5,6,7,8,9] 1차원 리스트
# num_arr=list(range(1,10))
# print(num_arr)
# all_arr=[]
# for i in range(0,9,3):
#     print(i) #0,3,6
#     all_arr.append(num_arr[i:i+3])
#     # all_arr.append(num_arr[0:3]) #0-3 / 0,1,2
#     # all_arr.append(num_arr[3:6]) #3-6 / 3,4,5
#     # all_arr.append(num_arr[6:9]) #6-9 / 6,7,8
# print(all_arr) #2차원 리스트 만듬.

# # 리스트안에 리스트 (2차원 리스트)
# # [
# #     [1,2,3],
# #     [4,5,6],
# #     [7,8,9]
# # ]