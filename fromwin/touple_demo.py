# 快捷鍵們
# 清除指令 cls
# 註解 ctrl+/
# 執行快捷鍵 ctrl+f5

# 可以存放非常多值 用小括號 = 元組, 中括號 =列表 list

#取位置 用[]
scores = (96,75,82,36,100)
print(scores[1])
print(scores[1:3])

#取長度
scores2 = (96,75,82,36,100,16,1674)
print(len(scores2))

#與列表的差別 創建元組後 就不能新增修改刪除
scores3 = (96,75,82,36,100)
scores3[0]=99
print(scores3)
#TypeError: 'tuple' object does not support item assignment

#元組資料存放不修改
#例如 101的座標
data = (13123132,1651311)
