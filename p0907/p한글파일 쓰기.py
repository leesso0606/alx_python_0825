

# import os
# #  r:파일 읽기 / w:파일 덮어 쓰기 / a:이어쓰기
# # 없는 폴더에 파일저장시 에러

# fname=input("저장할 파일이름을 입력하세요.(파일명)>>")



# if not os.path.exists("common"): #폴더가 있는지 확인.
#     os.makedirs("common") #폴더를 생성해줌

# with open("common/"+fname,"a",encoding="utf-8") as f:
#     while True:
#         line=input("글을 입력하시오.>>")
#         if line!="":
#             f.writelines(line+"\n") #\r:문장끝으로, \n:줄바꿈을 해라.
#         else: break

# print("파일이 저장되었습니다.")



# -------------------------------


# import os
# # r:읽기 / w: 쓰기/ a:이어쓰기

# with open("C:/aaa/a.txt","a") as f:
#     while True:
#         outStr=input("내용입력:")
#         if outStr=="": break #공백일때 정지
#         f.write(outStr+"\n") # 강제로 엔터키를 포함한것. 없으면 옆으로 계속 붙어서 출력됨.
#         # f.write(outStr)

# print("파일내용이 저장되었습니다.")
