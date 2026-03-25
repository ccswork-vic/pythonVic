# print(type(n1)) 檢查變速type的方式
# 快捷鍵們
# 清除指令 cls
# 註解 ctrl+/
# 執行快捷鍵 ctrl+f5

#for 迴圈

# for 變數 in 字串OR列表:
#     要重負執行的程式碼

# for letter in "小白你好":
#     print(letter)


# for num in[0,1,2,3,4,5]:
#     print(num)


# for num2 in range(6): #等於上面的 0~5
#     print(num2)


# for i in range(6): #等於上面的 0~5
#     print(i)



#[2,3,4,5,6]
for num2 in range(15,41): #等於上面的 2,3,4,5,6
    print(num2)

# print(pow(2,6)) #2*2*2*2*2*2


def power(n1,n2):  
    calc = n1
    for i in range(n2 - 1): #2的5次方 = 2*(2*2*2*2) 所以才會n2-1
        calc = calc *n1
    return calc

n1 = int(input("請輸入一個數： "))
n2 = int(input("請輸入要運算幾次數： "))
result =power(n1,n2)
print(result)
2*2*2*2*2
