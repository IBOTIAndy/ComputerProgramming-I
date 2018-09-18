def computeScore(CN, CSI, PD):
    total = (CN+CSI+PD)
    average = total//3
    return total, average

def main():
    name = input()      #名稱
    ID = int(input())   #學號
    CN = int(input())   #國文
    CSI = int(input())  #計概
    PD = int(input())   #計算機程式設計
    total, averageScore = computeScore(CN, CSI, PD)
    print('Name:%s' %name)
    print('ID:%d' %ID)
    print('Total:%d' %total)
    print('AverageScore:%d' %averageScore)

main()