# print(type(n1)) 檢查變速type的方式
# 快捷鍵們
# 清除指令 cls
# 註解 ctrl+/
# 執行快捷鍵 ctrl+f5

#類別class 物件 object
class phone:
    def __init__(self,os,number,is_waterproof,brand):
        self.os =os
        self.number = number
        self.is_waterproof = is_waterproof
        self.brand = brand
        
phone1 = phone("ios",5566,True,"Apple")

print(phone1.brand)

phone2 = phone("ADR",123,False,"htc")

print("手機廠牌:"+ str(phone2.brand)+ "," + "是否防水:"+str(phone2.is_waterproof)+ ",")