# print(type(n1)) 檢查變速type的方式
# 快捷鍵們
# 清除指令 cls
# 註解 ctrl+/
# 執行快捷鍵 ctrl+f5

#猜數字遊戲 一開始設定一個謎底，讓使用者輸入數字 提示大一點或小一點，直到猜中

# answer = 56
# guess_num =None

# while answer != guess_num:
#     guess_num= int(input("請輸入數字: "))
#     if guess_num > answer:
#         print("小一點")
#     elif guess_num < answer:
#         print("大一點")        
# print("你猜中拉!!!")

#進階款 多一個限制 只能被猜幾次


answer = 56
guess_num =None
guess_count = 0
guess_limit = 3
out_of_limit = False

while answer != guess_num and not(out_of_limit):
    guess_count += 1
    if guess_count <= guess_limit:
        guess_num= int(input("請輸入數字: "))
        if guess_num > answer:
            print("小一點")
        elif guess_num < answer:
            print("大一點")
    else:
        out_of_limit = True

if out_of_limit:
    print("你輸了")
else:
    print("你猜中拉!!!")

