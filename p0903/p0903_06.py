#  상품종류
s_arr = [
    {"prd_name":"컴퓨터","price":1000000},
    {"prd_name":"냉장고","price":2000000},
    {"prd_name":"오디오","price":500000},
    {"prd_name":"세탁기","price":1500000}
    ] # 1-0,2-1,3-2

# 나의 정보
my_info={"money":10000000}




#  함수 선언

def cal1():
    no=int(input(f"{s_arr[choice-1]["prd_name"]}을 구매하시겠습까?(구매:1,취소:0)"))
    if no==1:
        print("구매완료")
        # 구매한 후 나의 금액
        my_info["money"]=my_info["money"]-s_arr[choice-1]["price"]
        print(f"남은금액: {my_info["money"]}")
    else:
        print("구매하지 않습니다.")


# >>>>  프로그램 시작

# 상품명 출력
for i,p in enumerate(s_arr):
    print(f"{i+1}.{s_arr[i]["prd_name"]}:{s_arr[i]["price"]:,}원")

# print("1.컴퓨터-1000000")
# print("2.냉장고")
# print("3.오디오")
# print("4.세탁기")


choice = int(input("원하는 번호입력 : "))
if choice == 1:
    cal1()
elif choice == 2:
    cal1()
elif choice == 3:
    cal1()
elif choice == 4:
    cal1()
