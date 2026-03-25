# # 快捷鍵們
# # 清除指令 cls
# # 註解 ctrl+/
# # 執行快捷鍵 ctrl+f5

# #if判斷句

# #1
# #如果我肚子餓
# #就去吃飯
# hungry =True
# if hungry:
#     print("我就去吃飯")

# #2
# # 如果  今天下雨
# #       就開車去上班
# # 否則  
# #       就走路上班

# rainy = True
# if rainy:
#     print("就開車去上班")
# else:
#     print("就走路去上班")


# #3
# #如果 你考100分
# #   我給你1000元
# #或是如果 你考80分以上
# #   我給你500元
# #或是如果 你考60分以上
# #   我給你100元
# #否則
# #   你給我300元
# score =49
# if score ==100:
#     print("我給你1000元")
# elif score >= 80:
#     print("我給你500元")
# elif score >= 60:
#     print("我給你100元")
# else:
#     print("你給我300元")


# #4.
# #如果你考100分 且今天下雨
# #   我給你5566元
# #否則
# #   你給我88
# score =90
# rainy = True
# if score ==100 and rainy:
#     print ("我給你5566元")
# else:
#     print("你給我88元")


# #5
# # 如果你考100分 或者 今天下雨
# #   我給你168元
# #否則
# #   你給我777元
# score =90
# rainy =False
# if score ==100 or rainy:
#     print("我給你168元")
# else:
#     print("你給我777元")

# #6
# # 如果你考100分 或者 今天沒下雨
# #   我給你499元
# #否則
# #   你給我666元

# score = 100
# rainy =True
# if score ==100 or not(rainy):
#     print("我給你499元")
# else:
#     print("你給我666元")
# #7
# # 如果你沒有考100分 或者 今天沒下雨
# #   我給你777元
# #否則
# #   你給我888元
# score = 100
# rainy =True
# if score !=100 or not(rainy):
#     print("我給你777元")
# else:
#     print("你給我888元")

#傳入三個數字 回傳哪個數字最大
def max_num(n1,n2,n3):
    if n1>=n2 and n1>=n3:
        return n1
    elif n2>=n1 and n2>=n3:
        return n2
    else:
        return n3
n1 = int(input("請輸入第一個數字："))
n2 = int(input("請輸入第二個數字："))
n3 = int(input("請輸入第三個數字："))
# print(type(n1))
# print(type(n2))
# print(type(n3))
#print( max_num(n1,n2,n3))
print("最大的數字是"+ str(max_num(n1,n2,n3)))



#傳入一個list數字 回傳哪個數字最大

N = int(input("請輸入你要輸入幾個數字:"))
numbers =[] #存下輸入的值
sum = 0
for i in range(N):
    tmp = int(input("請輸入第"+str(i+1) + "個數字:"))
    numbers.append(tmp) # 將輸入的數字添加到列表中
    sum = sum + tmp

max_number =max(numbers)
print("以下是你輸入的數字列表",numbers , "最大數 :" + str(max_number)) 
print("sum = ",sum)


