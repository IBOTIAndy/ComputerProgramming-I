#奇偶數的判斷
def OddOrEven(num):     #判斷為奇數還是偶數
    odd = num % 2       #如果是奇數，除二的餘數將會是 1
    if odd:             #
        print("odd")    #
    else:               #
        print("even")   #
#---------------------------------
def main():
    number = int(input())   #輸入一個數
    OddOrEven(number)       #判斷該數為奇數還是偶數
#---------------------------------
main()