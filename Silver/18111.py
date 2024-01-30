#pypy3으로 통과
import sys
N, M, B = map(int, input().split())
ground = []
ans = int(1e9)
maxnum =0
for _ in range(N):
    ms = [int(x) for x in sys.stdin.readline().rstrip().split()]
    if maxnum < max(ms):
        maxnum = max(ms)
    ground.append(ms)

for i in range(maxnum+1):
    useBlock = 0
    takeBlock = 0
    for x in range(N):
        for y in range(M):
            if ground[x][y] > i:
                takeBlock += ground[x][y]-i
            else:
                useBlock += i-ground[x][y]
    if useBlock > takeBlock + B:
        continue

    cnt = takeBlock *2 + useBlock

    if cnt <= ans:
        ans = cnt
        glevel = i
print(ans, glevel)
