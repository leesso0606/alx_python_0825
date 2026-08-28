paper="""\
네팔 대홍수 참사 수습이 언제 끝날지도 모르는 상황에서 2차 홍수가 덮칠 수 있다는 관측이 나오고 있습니다. 
이번 홍수의 원인으로 지목된 것처럼 산 위의 빙하가 붕괴되면서 비 한 방울 없이 홍수가 또 일어날 수 있다는 겁니다.\
"""

print(paper)
print(len(paper)) #127

str1="1,홍길동,100,100,100,300,100" #타입-문자열
s=str1.split(",") #split:특정문자를 기준으로 분리를 해줌
print(s) #리스트로 분리됨. ['1', '홍길동', '100', '100', '100', '300', '100']
print(s[2]) #100

str2="2026-08-28"
s2=str2.split("-")
print(s2[0]) #2026

str3= "안녕 반가워 다음에 봐"
s3=str3.split(" ")
print(s3)
print(str3[1])

str4="EDMS,307-2E-PS-W-611-W008,VF5770"
s4=str4.split(",")
print(s4[2])

# strip - 공백제거
aaa1="   안녕하세요"
print(aaa1)
print(aaa1.strip()) #안녕하세요 로 공백없이 출력

aaa2="  안녕  하세요  "
print(aaa2.strip()) # 글자 사이의 공백은 지워지지 않음.
