import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
didntHear = set()

for _ in range(N):
    didntHear.add(input().strip())

target = []
for _ in range(M):
    name = input().strip()
    if name in didntHear:
        target.append(name)

target.sort()
length = len(target)

print(str(length)+'\n')
print('\n'.join(target))
