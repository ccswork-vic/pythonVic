# 快捷鍵們
# 清除指令 cls
# 註解 ctrl+/
# 執行快捷鍵 ctrl+f5

# #建立一個計算機
# num1 = float(input("請輸入第一個數： "))
# op = input("請輸入運算符號： ")
# num2 = float(input("請輸入第二個數： "))

# if op =="+":
#     print(num1+num2) 
# elif op =="-":
#     print(num1+num2) 
# elif op =="*":
#     print(num1*num2)
# elif op =="/":
#     print(num1/num2)  
# else:
#     print("不支援的運算")

#另一種寫法 練立一個函式
from math import * 
def calc(num1,op,num2):  
    if op =="+":
        return num1+num2
    elif op=="-":
        return num1+num2
    elif op=="*":
        return num1*num2
    elif op=="/":
        return num1/num2
    
num1 = float(input("請輸入第一個數： "))
op = input("請輸入運算符號： ")
num2 = float(input("請輸入第二個數： "))

result = floor(calc(num1,op,num2)) #用一個變數存下結果，呼叫calc並帶入三個值
# calc(num1, op, num2): 調用 calc 函數，將 num1、op 和 num2 傳遞給這個函數。

# 在 calc 函數內部，根據提供的 op（運算符號）執行相應的計算，然後返回計算結果。

# 將計算結果存儲在 result 變數中。


print("計算結果",result)