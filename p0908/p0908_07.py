
# 다른 폴더 안에 있는 파일 경우: from으로 import해야함
# from 폴더명 import 파일명
from project import students
from project import student

#  파일명.class명()

stus=students.Students()
# stus.slist =[]
# print(len(stus.slist))

# stus.slist =[s1]
s1=student.Student(1,"홍길동",100,100,99)
stus.add(s1)
stus.add(student.Student(2,"유관순",90,90,91))

stus.print()
