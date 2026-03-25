# 快捷鍵們
# 清除指令 cls
# 註解 ctrl+/
# 執行快捷鍵 ctrl+f5

# 列表list 
# 假設存放班級五位學生的成績
# score1 = 90
# score2 = 70
# score3 = 65
# score4 = 55
# score5 = 67
scores = [90,70,65,55,67]
print (scores)

#存放字串或布林值也行
friends =["jon","ADR","TOE",5566,True]
print(friends)

#取列表的值 第四位
scores = [90,70,65,55,67]
print (scores[4])
#從倒數取 用負數
scores = [90,70,65,55,67]
print (scores[-4])
#取列表多位
scores = [90,70,65,55,67]
print (scores[0:2])  #從第0位取到第二位之前，不包含第二位
print (scores[2:5])  #從第2位取到第5位之前，不包含第5位
print (scores[1:])   #從第1位取到list結束
print (scores[:4])   #取得第四位往前 不包含第四位所有值

phase = "hello Mr.Vic"
       # 0123456   
#取hello       
print(phase[0:5])
#取mr.vic
print(phase[6:])

#修改列表資料 第0位 改數字
scores = [90,70,65,55,67]
scores[0] =89
print (scores)

#extend 延伸 scores4加上friend2
scores4 = [90,70,65,55,67]
friends2 =["jon","ADR","TOE"]
scores4.extend(friends2)
print(scores4)


#append 再加上個值
scores5 = [90,70,65,55,67]
friends2 =["jon","ADR","TOE"]
scores5.append(9956)
print(scores5)

#insert 第四個位置 插入5566
scores6 = [90,70,65,55,67]
scores6.insert(4,5566)
print(scores6)

#remove 移除特定值
scores7 = [90,55,65,55,67,100,1262,1531,15]
scores7.remove(55)
print(scores7)


#remove 移除相同特定值
scores7 = [90,55,65,55,99,64,99,55,67,98]
for i in range(len(scores7)-1,-1,-1):
    if scores7[i] == 55 : #and scores7[i] == 99:
       scores7.remove(55)
for i in range(len(scores7)-1,-1,-1):
    if scores7[i] == 99 :
       scores7.remove(99)
print(scores7)

#clear 清除全部
scores8 = [90,55,65,55,67]
scores8.clear()
print(scores8)

#pop 移除列表最後一位
scores9 = [90,55,65,1561651,67]
scores9.pop()
print(scores9)

#sort 排序 asc 由小到大
scores9 = [90,55,165,1561651,617]
scores9.sort()
print(scores9)

#reverse 反轉
scores10 = [490,161,165,151,6197]
scores10.reverse()
print(scores10)

#index 想找的值
scores11 = [490,161,165,151,6197]
print(scores11.index(6197))

#count 數有多少個
scores12 = [490,161,165,151,6197,16516,151,1674,151]
print(scores12.count(151))




