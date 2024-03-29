N, K = map(int, input().split())
dp = [[0]*(K+1) for _ in range(N+1)]
info = [[0,0]]
for i in range(N):
    W, V = map(int, input().split())
    info.append([W, V])

for i in range(1, N+1):
    for j in range(1, K+1):
        w = info[i][0]
        v = info[i][1]

        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(dp[N][K])
