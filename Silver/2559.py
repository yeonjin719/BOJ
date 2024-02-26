n, k = map(int, input().split())
temp = list(map(int, input().split()))
dp = [0]*(n-k+1)
dp[0] = sum(temp[:k])
maxN = dp[0]
for i in range(1, n-k+1):
    dp[i] = dp[i-1]+temp[k+i-1]-temp[i-1]
    if dp[i] > maxN:
        maxN = dp[i]

print(maxN)
