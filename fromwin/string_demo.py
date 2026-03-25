# 快捷鍵們
# 清除指令 cls
# 註解 ctrl+/
# 執行快捷鍵 ctrl+f5
# 使用字串 字串的用法

#\n 換行
print("hello \nMR WHITE")

# 字串中印出雙引號"
# \" 就跳脫雙引號了
print("hello\" MR.WHITE")

#字串的相連
phrase ="hello "
print (phrase + "MR.black")
print("hello " + "vic")
#函式 lower 全部變小寫
phrase = "HELLOo MR.VIC"
print(phrase.lower())
#函式 upper 全部變大寫
phrase = "you good!"
print(phrase.upper())
#函式 isupper / islower 判斷是不是大小寫
vic = "you good!"
print(vic.isupper())
vic = "you good!"
print(vic.islower())

#函式疊加 先轉小寫 再判斷是不是都小寫
vic = "HELLOo MR.joN"
print(vic.lower().islower())

#中括號用法
VOC = "HI,AI!FIRST"
print(VOC[2])

# index查字串內位置在哪邊，如果有很多個會回傳第一個位置
VAC = "HI,AI!FIRST"
print(VAC.index("R"))

#replace 替換找到的字 前面是目標 後面是替換的結果
jon = "HELLO , VIC AND JON"
print(jon.replace("N",'Y'))

