#判斷何種三角形 輸入三角形的三個邊長，判斷是哪一種三角形
#IBOTIAndy 2018/09/18
def Triangle(a, b, c):  #判斷可不可以成為三角形
    if ((a + b) > c and (a + c) > b and (b + c) > a):   #如果任兩邊的和 大於第三邊
        return True     #可成為三角形
    else:               #
        return False    #
#
def Equilateral(a, b, c):   #判斷是否為正三角形
    if(a == b and b == c):  #三個邊等長
        return True         #
    else:                   #
        return False        #
#
def Isosceles(a, b, c):             #判斷是否為等腰三角形
    if(a == b or b == c or a == c): #其中兩個邊的長度相等
        return True                 #
    else:                           #
        return False                #
#---------------------------------
def Run(a, b, c):                           #
    if Triangle(a, b, c):                   #是否為三角形
        if Equilateral(a, b, c):            #是否為正三角形
            print("equilateral triangle")   #
        elif Isosceles(a, b, c):            #是否為等腰三角形
            print("isosceles triangle")     #
        else:                               #普通三角形
            print("triangle")               #
    else:                                   #不能構成三角形
        print("not triangle")               #
#---------------------------------
def test():             #測試資料
    print("4, 1, 1")    #
    Run(4, 1, 1)        #not triangle
    print("3, 3, 3")    #
    Run(3, 3, 3)        #equilateral triangle
    print("3, 2, 3")    #
    Run(3, 2, 3)        #isosceles triangle
    print("7, 8, 9")    #
    Run(7, 8, 9)        #triangle
#---------------------------------
def main():
    a, b, c = map(int, input().split()) #定義三個邊，並使用連續輸入
    Run(a, b, c)                        #開始執行
    #test()  #測試用Funtion
#=================================
main()