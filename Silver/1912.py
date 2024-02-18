import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
num = list(map(int, input().split()))
dp = [0]*n


for i in range(n):
    if i>0:
        dp[i] = max(dp[i-1]+num[i], num[i])
    else:
        dp[i] = num[0]

print(str(max(dp)))
