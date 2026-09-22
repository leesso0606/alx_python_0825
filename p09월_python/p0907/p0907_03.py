

# ----------------------------------------

# common폴더 안에 stu.txt로 파일을 저장하시오.
# 1
# 홍길동
# 100
# 100
# 100
# 300
# 100.0 형태로 저장

# with open("C:/workspace/python/alx_python_0825/common/stu.txt","w",encoding="utf-8") as f:
#     while True:
#         line=input("정보를 입력하시오")
#         if line=="": break
#         else:
#             f.write(line+"\n")
#     print("저장 완료 되었습니다.")


# 1,홍길동,100,100,100,300,100.0

with open("C:/workspace/python/alx_python_0825/common/stu.txt","a",encoding="utf-8") as f:
    allStr=""
    no=0
    while True:
        outStr=input("내용입력: ")   # 1,홍,100,100
        if no==0:
            allStr=outStr
            no+=1
            continue
        if outStr=="": 
            f.write(allStr+"\n")
            break
        allStr= allStr+(","+outStr)
        no+=1 #1씩 증가
    print(allStr)



# with open("common/stu.txt","a",encoding="utf-8") as f:
# allStr = ""
# while True:
#     outStr = input("내용입력 : ")
#     if outStr == "":
#         f.write(allStr+"\n")
#         break
#     allStr += (outStr+",")
#     print(allStr)