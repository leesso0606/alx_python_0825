


from stufunc import *
from students import*
from student import*

# readStu() # 파일불러오기
while True:
    # 0.메인화면
    choice=main_screen()
    # choice=int(input("숫자를 입력하시오."))
    if choice == 1:
        stu_input()    # 1.학생성적입력함수
    elif choice == 2:
        stu_output()   # 2.학생성적출력함수
    elif choice == 3:
        stu_updata()
    elif choice==8:
        print("[등수처리]")
    elif choice == 9:
        writeStu()
    else:
        print("프로그램 종료")
        break





























# --------------------------------------------------------------------------




# from student import*
# from students import*

# # stus=Students()
# # student->Student클래스
# # 홍길동 성적->stus.add(s1)
# # 유관순 성적->stus.add(s2)

# # 리스트 class화
# # class Students:
# #     stuList=[]

# #     def __init__(self,s):
# #         self.list.append(s) #s 정보를 list에 넣는다.

# #     def add(self,s):
# #         self.list.append(s) #s 정보를 list에 더하는 함수.




# stu=Students(Student(1,"홍길동",100,100,100))
# stu.add(Student(2,"유관순",100,100,100))
# for ss in stu.stuList:
#     print(ss)



# # 1.---------------------------------------------
# stuList=[]

# # student -> Student 클래스
# # 홍길동 성적 -> stuList.append(s1)
# # 유관순 성적 -> stuList.append(s2)

# s1=Student(1,"홍길동",100,100,100)
# s2=Student(2,"유관순",100,100,100)

# stuList.append(s1)
# stuList.append(s2)
# for s in stuList:
#     print(s)

# # 학생성적을 출력하시오
# # for문 사용을 해서 출력하시오.

