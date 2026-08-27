import random
import datetime #현재 시간을 가져오는 클래스선언
# from datetime import datetime

# 현재시간
now = datetime.datetime.now()
print("전체:",now) #전체시간
print("년도:",now.year) #년도
print("월:",now.month) #월
print("일:",now.day) #일
print("시:",now.hour) #시
print("분:",now.minute) #분
print("초:",now.second) #초
print("초:{}".format(now.second))

# 2026년 8월27일 11시12분10초
# format함수사용
print("{}년{}월{}일{}시{}분{}초".format(2026,8,27,11,12,10))
print("{}년{}월{}일{}시{}분{}초".\
      format(now.year,now.month,now.day,now.hour,now.minute,now.second))