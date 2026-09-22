
# 변수, 리스트, 딕셔너리 선언부분

# >>변수 선언 부분
# 개인정보
my_info={"id":"aaa","pw":"1111",\
        "money":10_000_000,"bounsPoint":0}

# 구매리스트
cart=[]

# 상품정보
product=[
    {"p_name":"컴퓨터","price":1000000,"bounsPoint":1000000*0.1},
    {"p_name":"냉장고","price":2000000,"bounsPoint":2000000*0.1},
    {"p_name":"오디오","price":5000000,"bounsPoint":500000*0.1}
]








# 함수


def cal1(choice):
    no=int(input(f"{product[choice-1]["p_name"]}를 구매하시겠습니까?(구매:1,취소:0) "))
    if no==1:
        print(f"{product[choice-1]["p_name"]}구매완료")
    
        # -- 계산 후 결과
        my_info["money"]-= product[choice-1]["price"]
        # my_info["money"] =my_info["money"]-product[0]["price"]
    
        my_info["bounsPoint"] += product[choice-1]["bounsPoint"]
        print(f"m머니 : {my_info['money']:,}원")
        print(f"m보너스포인트: {my_info["bounsPoint"]:,}포인트")
        # print("p보너스포인트:",product[0]["bounsPoint"])
    else:
        print("이전화면으로 이동합니다.")







# >>프로그램 실행

# -- 아이디,패스워드 확인.

while True:
    print("[쇼핑몰에 오신것을 환영합니다.]")
    id=input("아이디:")
    pw=input("패스워드:")

    if my_info["id"]==id and my_info["pw"]==pw:
        print("로그인이 되었습니다.")
        break
    else:
        print("로그인에 실패하였습니다.")

# -- 현재 my 금액, 보너스 포인트

print(f"현재 보유 금액: {my_info["money"]:,}원")
print(f"현재 보너스포인트 : {my_info["bounsPoint"]:,}포인트")
print("-"*40)
# print("현재보유금액:",my_info["money"])
# print("현재 보너스포인트:",my_info["bounsPoint"])

# -- 구매정보
while True:
    print()
    # 상품 출력부분
    print("[쇼핑몰 구매 사이트]")
    for i,p in enumerate(product):
            print(f"{i+1}.{p["p_name"]}:{p["price"]:7,}원")
    print("9. 구매상품리스트")
    print("-"*30)
    choice=int(input("원하는 번호를 입력하세요.>>"))
    print()

    # print("1. 컴퓨터- 1000000")
    # print("2. 냉장고- 2000000")
    # print("3. 오디오- 500000")


    # 1. 컴퓨터 구매 부분

    if choice==1:
        cal1(choice)

    elif choice==2:
        cal1(choice)

    else:
        cal1(choice)
    








# -----------------------------------------------


# # 일반매개변수, 초기화매개변수
# # 가변매개변수, 키워드매개변수 / 거의 일반매개변수를 쓴다.


# def cal(s1=1,e1=50,s2=10): # 초기화 매개변수 : 값을 미리 세팅했다. / 매개변수가 다르면 에러가 나니까.
#     print(s1,e1,s2)

# cal() #1 50 10
# cal(100,1,2) #100 1 2
# cal(100) #100 50 10
# cal(1,2,s2=100) #1 2 100 
# cal(e1=20) #1 20 10



# --------------------------------------


# # 가변함수
# # 매개변수는 서로 값 개수가 맞아야 하는데
# # *매개변수(가변매개변수)를 붙이면 매개변수 개수가 안맞아도 상관없음.

# # 가변 매개변수 - 맨 뒤쪽에 배치
# # 키워드 매개변수 - 맨뒤쪽에 배치.
# # 가변 매개변수가 있던 없던 키워드 매개변수는 무조건 맨 뒤쪽에 위치.

# def str_print(*v,n): # 가변매개변수가 앞에 있을 때
#     print(n)    
# # 키워드 매개변수 :특정한 값을 지정한것.
# # 키워드 매개변수는 무조건 맨 뒤에 있어야 함.
# str_print(1,2,3,4,5,n="안녕")




# -------------------------------------


# # sep="--" : "" 안에 들어간 것이 구분자가 됨. 세퍼레이트
# print(1,2,3,4,5,sep="--")
# print("번호","이름","국어","영어",sep="\t")
# arr=["번호","이름","국어","영어"]
# print(*arr,sep="\t") # 전개연산자,키워드 매개변수





# ----------------------------------------------------------


# def str_print(n,*v): #매개변수 2개,뒤에것은 가변매개변수
#     for i in range(n):
#         for j in v:
#             print(j,end=" ")
#         print()

# str_print(3,"안녕","반가워","잘있어")

