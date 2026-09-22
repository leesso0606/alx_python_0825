no=input("번호를 입력하세요.")
name=input("이름을 입력하세요.")
a=int(input("국어점수"))
b=int(input("영어점수"))
c=int(input("수학점수"))
d=a+b+c
e=d%3


print("번호:{},이름:{},국어점수:{},영어점수:{},수학점수:{},합계:{},평균:{}".format(no,name,a,b,c,d,e))