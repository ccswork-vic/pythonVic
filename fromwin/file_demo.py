# print(type(n1)) 檢查變速type的方式
# 快捷鍵們
# 清除指令 cls
# 註解 ctrl+/
# 執行快捷鍵 ctrl+f5

#檔案讀取，寫入

# open("檔案路徑",mode="開啟模式")

#絕對路徑 ex C:/Users/vic/Documents/python/1234.txt
#相對路徑 程式的位置做延伸 ex 1234.txt


# mode="r" 讀取
# mode="w" 覆寫
# mode="a" 在原本資料後寫東西

# file = open("C:/Users/vic/Documents/python/1234.txt",mode="r")
# print(file.read())
# file.close()

#如果只要讀第幾行 寫一個讀一行
# file = open("C:/Users/vic/Documents/python/1234.txt",mode="r")
# print(file.readline())
# print(file.readline())
# file.close()

#讀出全部的行 用for來寫
# file = open("C:/Users/vic/Documents/python/1234.txt",mode="r")
# for line in file:
#     print(line)
# file.close()

# 把每一行資料 放到列表裡面 用/n換行
# file = open("C:/Users/vic/Documents/python/1234.txt",mode="r")
# print(file.readlines())
# file.close()

# mode="w" 覆寫
# file = open("123.txt",mode="w")
# file.write("vic add")
# file.close()


# mode="a" 在原本資料後寫東西
# file = open("123.txt",mode="w" ,encoding='utf-8')
# file.write("\n大家好")
# file.close()

#使用with來自動close
with open("123.txt" , mode="a",encoding='utf-8') as file:
    file.write("\n 9958595")

