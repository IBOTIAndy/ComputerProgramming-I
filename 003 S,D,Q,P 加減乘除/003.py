#003: two number for (+ - * /)
def Sum(num1, num2):        #加法
    sum = num1 + num2
    return sum;

def Difference(num1, num2): #減法
    difference = num1 - num2
    return difference;

def Product(num1, num2):    #乘法
    product = num1 * num2
    return product;

def Quotient(num1, num2):   #除法取商
    quotient = num1 / num2
    return quotient;

def AbsoluteValue(number): #加絕對值
    return abs(number)

def Math(num1, num2):               #數學運算函式
    sum = Sum(num1, num2)           #+
    dif = Difference(num1, num2)    #-
    pro = Product(num1, num2)       #*
    quo = Quotient(num1, num2)      #/
    dif = AbsoluteValue(dif)        #特殊需求:減法的複數要套絕對值
    return sum, dif, pro, quo
#---------------------------------
def output(sum, difference, product, quotient): #輸出
    print("Difference:%.2f" %difference)        #Difference:00.00
    print("Sum:%.2f" %sum)                      #Sum:00.00
    print("Quotient:%.2f" %quotient)            #Quotient:00.00
    print("Product:%.2f" %product)              #Product:00.00
#---------------------------------
def main():
    num1 = float(input("請輸入第一個數："))   #定義兩個浮點數
    num2 = float(input("請輸入第二個數："))
    sum, difference, product, quotient = Math(num1, num2)    #執行數學式
    output(sum, difference, product, quotient)  #輸出
#---------------------------------
main()