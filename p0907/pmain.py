
from pfunc import *
# 정보

stuList = []
title = ["번호","이름","국어","영어","수학","합계","평균","등수"]
s_title = ["no","name","kor","eng","math","total","avg","rank"]
stuNum = 1  #전역변수


# 파일 불러오기
readStu()

# 학생성적 프로그램

# 메인화면
while True:
    choice= main()
    if choice==1:
        stu_input()
    elif choice==2:
        stu_output()
        
    elif choice==3:
        pass
    elif choice==9:
        writeStu()
                
    elif choice==0:
        pass