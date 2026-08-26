money = 12340
# 12340 -> 500원 동전 몇개? 100원동전 몇개? 10원 동전 몇개?
# 12340원 500원동전:?, 100원동전?, 10원:?

result = money//500 #몫 24개
num= money%500 #나머지 340
result2 = num//100 # 몫 3
num2 = num%100 #나머지 4
result3 = num2//10 #몫 4
num3 = num%10 #나머지 0
print("500원:{}개, 100원{}개, 10원:{}개".format(result,result2,result3))



# # 500원 동전 몇개가 필요할까요?
# result = money//500
# print("500원동전 필요 개수:".format(result))
# print("500원동전 필요 개수:",(result))