T = int(input())
dp=[[1,0],[0,1],[1,1]]

def fibonacci(n):
    global cnt1, cnt0
    global answer
    if len(dp) > n+1:
        answer[0] += dp[n][0]
        answer[1] += dp[n][1]
    elif len(dp) == n:
        dp.append([dp[n-1][0]+dp[n-2][0],dp[n-1][1]+dp[n-2][1]])
        answer[0] += dp[n][0]
        answer[1] += dp[n][1]
    else:
        return fibonacci(n-1), fibonacci(n-2)
for i in range(T):
    N = int(input())
    answer = [0,0]
    if N == 0:
        print(1, 0)
    elif N == 1:
        print(0, 1)
    else:
        fibonacci(N)
        print(answer[0], answer[1])
