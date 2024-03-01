import sys
input = sys.stdin.readline

N, M = map(int, input().split())
woodLen = list(map(int, input().split()))
end = max(woodLen)
start = 0

while (end >= start):
    height = (end + start) // 2
    needWoodLen = 0
    for i in range(N):
        if woodLen[i] - height > 0:
            needWoodLen += woodLen[i]-height
    if needWoodLen >= M:
        start = height + 1
    else:
        end = height - 1
    

print(end)
