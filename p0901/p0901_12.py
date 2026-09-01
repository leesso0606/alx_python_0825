# 학생성적 프로그램
# 1. 번호,학생이름, 점수등 담을 수 있는 리스트 만들기

stu_list=[]

# 2. 무한으로 입력받기

while True:
    no=len(stu_list)+1 #no는 리스트 stu_list 주소 0부터+1한 값이 나옴.
    print("번호:",no)
    name=input("이름:(종료하려면 0):")
    if name=="0": 
        break
    kor=int(input("국어점수:"))
    eng=int(input("영어점수:"))
    math=int(input("수학점수:"))
    total=kor+eng+math
    avg=total/3
    stu_list.append([no,name,kor,eng,math,total,avg])
    print()
# print(stu_list)

# 3. 성적 출력받기
print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
print("-"*60)
for s in stu_list:
    print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*s))
