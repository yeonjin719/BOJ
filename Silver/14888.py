import sys
input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())
MaxNum = -1000000000
MinNum = 1000000000

def dfs(i, now, plus, minus, multiply, divide):
    global MaxNum, MinNum, num
    if i == N:
        MaxNum = max(MaxNum, now)
        MinNum = min(MinNum, now)
        return
    else:
        if plus > 0:
            dfs(i+1, now+num[i], plus-1, minus, multiply, divide)
        if minus > 0:
            dfs(i+1, now-num[i], plus, minus-1, multiply, divide)
        if multiply > 0:
            dfs(i+1, now*num[i], plus, minus, multiply-1, divide)
        if divide > 0:
            if now < 0:
                now *= -1
                dfs(i+1, (now//num[i])*-1, plus, minus, multiply, divide-1)
            else:
                dfs(i+1, now//num[i], plus, minus, multiply, divide-1)


dfs(1, num[0], plus, minus, multiply, divide)
print(MaxNum)
print(MinNum)
