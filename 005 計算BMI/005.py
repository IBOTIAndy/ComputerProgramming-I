#005 BMI計算 輸入身高與體重，算出 BMI 為多少
#IBOTIAndy 2018/09/18
import math #數學函式庫,用來使用次方
#
def Input():            #輸入
    M = float(input())  #輸入身高
    Kg = float(input()) #輸入體重
    return M, Kg        
#---------------------------------
def BMIMath(M, Kg):             #計算BMI
    BMI = Kg / math.pow(M,2)    #BMI = kg / m * m (公斤/公尺^2)
    return BMI              
#---------------------------------
def Output(BMI):        #輸出
    print("%.1f" %BMI)  #輸出BMI
#---------------------------------
def test():                     #測試用程式
    print("1.72m & 60kg")       #輸出輸入的資料
    BMI = BMIMath(1.72, 60.0)   #計算BMI
    Output(BMI)                 #輸出BMI
#---------------------------------
def main():                 #
    M, Kg = Input()         #輸入身高體重
    BMI = BMIMath(M, Kg)    #計算BMI
    Output(BMI)             #輸出BMI
    #test()  #測試用Funtion
#=================================
main()