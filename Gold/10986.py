N, M = map(int, input().split())
nums = list(map(int, input().split()))
arr = [0] * M
cnt = 0
for i in range(N):
    cnt += nums[i]
    arr[cnt%M] += 1

ans = arr[0]

for i in arr:
  ans += i*(i-1)//2

print(ans)
