import sys
input = sys.stdin.readline
def findNum(num):
    if num == 0 or num == 1:
        return 2
    isNot = True
    while True:
        if isNot == False:
            return num
        isNot = False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                isNot = True
                break
        if isNot == True:
            num += 1


n = int(input())
for i in range(n):
    num = int(input())
    print(findNum(num))