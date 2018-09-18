#002 一元二次方程式，ax^2 + bx + c：輸入a, b, c，求實根
#IBOTIAndy 2018/09/18
import math #引入數學式(math)來使用開根號(sqrt())

def RealNumber(a, b, c):    #求 aX^2 + bx + c = 0 的實根
    return (((-b) + math.sqrt(b * b - 4 * a * c)) / (2 * a))

def Math(a, b, c):              #數學式 
    x1 = RealNumber(a, b, c)    #求x1的實根 ((-b)+sqrt(b*b-4*a*c))/(2*a) 
    x2 = RealNumber(a, b, c)    #求x2的實根 ((-b)+sqrt(b*b-4*a*c))/(2*a) 
    return x1, x2               
#---------------------------------
def output(x1, x2):     #輸出
    print("%.1f" %x1)   #x.0
    print("%.1f" %x2)   #x.0
#---------------------------------
def main():
    a = int(input())        #定義常數a, b, c
    b = int(input())        #
    c = int(input())        #
    x1, x2 = Math(a, b, c)  #求實根的數學式
    output(x1, x2)          #輸出
#=================================
main()