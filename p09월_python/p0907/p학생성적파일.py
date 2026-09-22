

import p09월_python.p0907.p_stu_m as p_stu_m
import p09월_python.p0907.p_stu_m as pm
from p09월_python.p0907.p_stu_m import main_screen,stu_input,stu_output,readStu,writeStu
# from p_stu_m import* # 모든 함수 불러오기






readStu() #  파일 불러오기
while True:
    choice=main_screen()
    if choice==1:
        stu_input()
    elif choice==2:
        stu_output()
    elif choice==3:
        pass
    elif choice==9:
        writeStu()