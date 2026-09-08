# 일반적인 프로그램
# 다른 조건이나 같은 프로그램 다른 변수를 쓸때면 다시 변수 지정으로 2배사용 해야함.
# 하지만 class는 c=car()을 c2=car()식으로 가져와 사용가능.
color=""
speed=0

def upSpeed():
    global speed
    speed+=10

def downSpeed():
    global speed
    speed-=10

color="whith"
print("색상:",color)
print("속도:",speed)

upSpeed()
print("속도2:",speed)

# ---------------------------------------


color2=""
speed2=0

def upSpeed2():
    global speed2
    speed2+=10

def downSpeed2():
    global speed2
    speed2-=10

color2="whith"
print("색상:",color2)
print("속도:",speed2)

upSpeed2()
print("속도2:",speed2)
