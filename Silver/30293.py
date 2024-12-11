import sys
print = sys.stdout.write
input = sys.stdin.readline
N = int(input())
target = list(map(int, input().split()))
cnt = 0

for i in range(N):
  if i == 0:
    cnt += abs(target[0])
    P = [target[0] for _ in range(N)]

  else:
    diff = target[i]-P[i]
    for j in range(1, (N//(i+1))+1):
      P[((i+1)*j)-1] += diff
    cnt += abs(diff)

if P != target:
  print(str(-1))
else:
  print(str(cnt))