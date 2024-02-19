import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input().rstrip())
dp = [0]*(n+1)

stair = [0]*(n+1)

for i in range(1,n+1):
    stair[i] = (int(input().rstrip()))

if n == 1:
    dp[1] = stair[1]

if n == 2:
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2]

if n+1 >= 4:
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2]
    dp[3] = max(stair[1]+stair[3], stair[2]+stair[3])

    for i in range(4, n+1):
        dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])


print(str(dp[n]))
