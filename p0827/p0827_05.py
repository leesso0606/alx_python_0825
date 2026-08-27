






# import datetime
# now=datetime.datetime.now()
# print(now)
# print(now.year)
# print(now.month)

# # 월을 출력하는데, 1,2,3,...9월->01월,02월..10월 식으로 2자로 찍혔으면 좋겠음.
# print("{:02d}월".format(now.month))
# print("{:02}월".format(now.month))
# print("{:02}분".format(now.minute))
# print("{:02d}초".format(now.second))

# # 2026년8월27일 11시57분20초
# print(now)
# f_date=now.strftime("%Y/%m/%d") # 원하는 모양으로 변경가능.. 하지만 잘 쓰지않음.
# f_date=now.strftime("%Y년%m월%d일")
# print(f_date)


# format
# 123->5자리 빈 공뱅 0으로 채워서 출력하시오.
# print("{:05}".format(123))
# print("{:05d}".format(123))
# print("{:05,d}".format(12345)) # ,를 넣으면 1000단위 표시를 할 수 있음
