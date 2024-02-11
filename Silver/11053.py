import sys
input = sys.stdin.readline
print = sys.stdout.write
N = int(input())
A = list(map(int, input().rstrip().split()))

dp =[1]*N

for i in range(1, N):
    for j in range(0, i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(str(max(dp)))
