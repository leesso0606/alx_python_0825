# 1. 번호, 이름, 국어, 영어, 수학
# 2. 합계, 평균을 구한다음
# 3. 성적출력하도록 구성하시오

# 입력: input -> 변수저장 ->DB저장(이부분 배울 예정)
s=[0,0,0,0,0,0,0] #리스트타입->append,insert / pop,del,remove
s[0]=input("번호:") #str #==s.append(input("번호:"))
s[1]=input("이름")
s[2]=int(input("국어점수:")) #int
s[3]=int(input("국어점수:")) #int
s[4]=int(input("국어점수:")) #int
s[5]=s[2]+s[3]+s[4]
s[6]=s[5]/3 #나눗셉->float(실수형)

print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
print("-"*60) # 문자*:문자반복
print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}")
print("{}\t{}\t{}\t{}\t{}\t{:d}\t{:2f}".format(s[0],s[1],s[2],s[3],s[4],s[5],s[6]))