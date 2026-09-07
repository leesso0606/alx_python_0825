import func #파일(모듈)불러오기
# func.함수명 : 파일명 안에 있는 함수를 불러와라

import func as fn
# fn.함수명

from func import hap1,hap2,hap3
#  함수명만 사용하면됨, 저 파일안 특정 함수만 끌어오는 것.


#1.  두수를 입력받아 두수의 합을 구하시오.
# 매개변수 x, 리턴도 없음

func.hap1()



#2.  두수를 입력받아 두수의 합을 구하시오.
# 매개변수 있고 리턴값없음
num3=int(input("숫자입력1:"))
num4=int(input("숫자입력2:"))
fn.hap2(num3,num4)



#3.  두수를 입력받아 두수의 합을 구하시오.
# 매개변수 있고 리턴도 있음.
num5=int(input("숫자입력1:"))
num6=int(input("숫자입력2:"))
sum=hap3(num5,num6) # sum 값을 받음
print(sum)