import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
dp = [[0]*i for i in range(1,n+1)]
a = []
for i in range(n):
    a.append(list(map(int, input().rstrip().split())))
dp[0][0] = a[0][0]

for i in range(1, n):
    for j in range(len(a[i])):
        if j == 0:
            dp[i][j] += a[i][j] + dp[i-1][0]
        elif j == len(a[i])-1:
            dp[i][j] += a[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] += a[i][j] + max(dp[i-1][j-1], dp[i-1][j])

print(str(max(dp[-1])))
