#001 輸入 (國文, 計算機概論, 計算機程式設計) 的三個成績，算出加總與平均
#IBOTIAndy 2018/09/18
def computeScore(CN, CS, PD):   #成績計算器
    total = (CN+CS+PD)          #成績加總
    average = total//3          #成績平均
    return total, average       #
#---------------------------------
def main():
    name = input()      #名稱
    ID = int(input())   #學號
    CN = int(input())   #國文
    CS = int(input())   #計算機概論
    PD = int(input())   #計算機程式設計
    total, averageScore = computeScore(CN, CS, PD)  #計算總和與平均
    print("Name:%s" %name)                  #Name:xxxx
    print("ID:%d" %ID)                      #ID:1055900xx
    print("Total:%d" %total)                #Total:300
    print("AverageScore:%d" %averageScore)  #AverageScore:100
#=================================
main()