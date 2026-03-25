# 快捷鍵們
# 清除指令 cls
# 註解 ctrl+/
# 執行快捷鍵 ctrl+f5

# 如何使用數字、數字的用法
#基本使用
print(77)
print(669.123113)
print(-4984)
print(9+6)
print(119-260)
print(18*48)
#一般除法 會有小數點
print(100/5)
#整數除法  不會有想小數點兩個//
print(100//6)

#連續運算 先乘除後加減
print (9+8*5/2)

#掛號的算法
print ((9+8)*5/2)

#取餘數 用%
number =8
print(number%5)

#函式 str 轉字串
sifo = 99.5
print("會印出會印出數字 " + str(sifo))

phrase ="hello "
num4 = '996'
print (phrase + "MR.black")
print( 'test ' + num4 + " vic " + phrase)

#函式 abs 取絕對值
num = -9964919
print(abs(num))

#函式 pow 次方 範例是8的三次方
num2 = 10
num3 = pow(num2,3)
print(num3) 

#函式 max 告訴我們哪個數最大
print(max(2,3,151,5566))
print(max(2,3,num3,55))

#函是 min 回傳最小的數字
print(min(0,num,sifo,-15651))

#函式 round 四捨五入
print(round(4.6))

#拿到更多數學函式
from math import * 

#無條件捨去 floor
print(floor(69.8))

#無條件進位 ceil
print(ceil(99.8))

#開根號 sqrt
print(sqrt(25))