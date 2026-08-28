# 1. 번호, 이름, 국어, 영어, 수학
# 2. 합계, 평균을 구한다음
# 3. 성적출력하도록 구성하시오

# 입력: input -> 변수저장 ->DB저장(이부분 배울 예정)
s=[] #리스트타입->append,insert / pop,del,remove
no=input("번호:") #str
name=input("이름")
kor=int(input("국어점수:")) #int
eng=int(input("국어점수:")) #int
math=int(input("국어점수:")) #int
total=kor+eng+math
avg=total/3 #나눗셉->float(실수형)

print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
print("-"*60) # 문자*:문자반복
print(f"{no}\t{name}\t{kor}\t{eng}\t{math}\t{total}\t{avg:.2f}")
print("{}\t{}\t{}\t{}\t{}\t{}\t{:2f}".format(no,name,kor,eng,math,total,avg))