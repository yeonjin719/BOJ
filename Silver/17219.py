import sys
iniput = sys.stdin.readline
print = sys.stdout.write
N, M = map(int, input().split())
info = {}
for i in range(N):
    site, pw = input().split(' ')
    info[site] = pw

for i in range(M):
    find = input().rstrip()
    print(info[find])
    print('\n')
