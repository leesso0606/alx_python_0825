

# slist=[]
# title=["번호","이름","국어","수학","영어","합계","평균","등수"]
# s_title = ["no","name","kor","eng","math","total","avg","rank"]


from stuFunc import*

sno=1
#  파일 불러오기

readlist()


while True:
    choice=main()

    if choice==1:
        s_input()

    elif choice==2:
        s_output()
    elif choice==3:
        s_updata()

    elif choice==9:
        s_write()

    elif choice==0:

        pass
    