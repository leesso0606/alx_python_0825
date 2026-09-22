#  파일 복사하기
import os

rf=open("c:/aaa/1.jpg","rb") # rb:글로 읽지 않겠다.
wf=open("c:/aaa2/2.jpg","wb")

while True:
    fdata=rf.read(1)
    if not fdata:break #파일이 없으면 멈춘다.
    wf.write(fdata) #rf에 파일이 없을 때까지 읽고 wf에 쓴다.
rf.close()
wf.close()
print("이미지 파일이 복사되었습니다.")

# ---------------------------------------

rf2=open("c:/aaa/2.jpg","rb") # rb:글로 읽지 않겠다.
wf2=open("c:/aaa2/3.jpg","wb")
while True:
    fdata2=rf2.read(1)
    if not fdata2:break
    wf2.write(fdata2)
rf2.close()
wf2.close()
print("이미지 파일이 복사되었습니다.")
