


# 파일 읽어오기
# 파일 오픈하고 꼭 클로즈해야함

f=open("C:/aaa/test1.txt","r",encoding="utf-8") # r:읽어오기,encoding="utf-8":한글을

while True:
    line= f.readline()
    if not line:
        break
    else:
        print(line,end="")
f.close()

print()



# 아래 코드를 위 코드로 변경. 같은것.

# file1=open("C:\\aaa\\test1.txt","r",encoding="utf-8") # r:읽어오기,encoding="utf-8":한글을
# f1=file1.readline() #1줄 출력
# print(f1,end="") # end를 넣어 enter을 없앰
# f2=file1.readline()
# print(f2,end="")
# f3=file1.readline()
# print(f3,end="")
# file1.close()