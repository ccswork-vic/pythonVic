# 快捷鍵們
# 清除指令 cls
# 註解 ctrl+/
# 執行快捷鍵 ctrl+f5

#函式的定義

#定義一個hello函式 用來印出hello vic
def hello():  #命名規則 大小寫英文數字組合，開頭不能是數字
    print("hello vic") #前方要留白，往下寫要繼續留白 不然就不是函式內部

#函式的呼叫 你定義的函式名+()
hello()

#定義一個hello2函式 傳入參數
def hello2(name):  
    print("hello " + name) 

#函式的呼叫 你定義的函式名+()
hello2("vic5566")

#定義一個hello3函式 傳入多個參數
def hello3(name,date):  
    print("hello " + name + "今天是2023"+ str(date) ) #把數字轉string

#函式的呼叫 你定義的函式名+()
hello3("jon",1129)


#定義一個hello函式 傳入多個參數
def hello4(name,date):  
    print("hello " + name + "今天是2023"+ date ) 

#函式的呼叫 你定義的函式名+()
hello4("chiu","1128")#把date用成字串格式


#定義一個函示，傳入兩個數字，做出數字相加。
def add(num1,num2):
    print(num1+num2)

add(90,536)

#定義一個函示，傳入兩個數字，做出數字相加。加上回傳功能
def add2(num1,num2):
    #print(num1+num2)
    return 10 #回傳數字10 只要函式碰到reutrn 就會把呼叫的值覆蓋掉
add2(3,2)
print(add2(3,2))


#定義一個函示，傳入兩個數字，做出數字相加。加上回傳功能
def add3(num1,num2):
    return num1+num2  #只要函式碰到reutrn,就會把呼叫的值覆蓋掉
add3(30,20)
print(add3(30,20))


#考題 下列執行後會甚麼結果 5+9=14 reture 66

def vic(n1,n2):
    print(n1+n2)
    return 66

value =vic(5,9)
print(value)

#reture沒寫 會給出 none '95-5'=100 沒reture 所以給出 none

def vic2(n1,n2):
    print(n1+n2)
    
value =vic2(95,-5)
print(value)

#return後又加上print不處理，碰到return 就結束函式
def vic4(n1,n2):
    print(n1+n2)
    return "大家好"
    print("你好")
    
value =vic4(49,6)
print(value)


def add(num1,num2):
    print(num1+num2)

add(90,536)