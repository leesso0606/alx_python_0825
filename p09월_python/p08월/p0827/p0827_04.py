import random
import datetime #현재 시간을 가져오는 클래스선언
# from datetime import datetime


# if을 써서 1-6월까지는 상반기
# 7-12월까지는 하반기라고 출력.
# 현재월을 datetime함수를 사용해서 검색한 다음
# 상반기, 하반기인지 출력하시오

# 날짜 함수를 사용해서 월을 변수에 저장을 한후
# 비교, 출력

import datetime
now=datetime.datetime.now()
month=now.month
if month>6:
    print("하반기 입니다")
    print("{}월:하반기 입니다".format(month))
else:
    print("상반기 입니다")
    print("{}월:상반기 입니다".format(month))




# 현재시간
# now = datetime.datetime.now()
# print("전체:",now) #전체시간
# print("년도:",now.year) #년도
# print("월:",now.month) #월
# print("일:",now.day) #일
# print("시:",now.hour) #시
# print("분:",now.minute) #분
# print("초:",now.second) #초
# print("초:{}".format(now.second))

# # 2026년 8월27일 11시12분10초
# # format함수사용
# print("{}년{}월{}일{}시{}분{}초".format(2026,8,27,11,12,10))
# print("{}년{}월{}일{}시{}분{}초".\
#       format(now.year,now.month,now.day,now.hour,now.minute,now.second))