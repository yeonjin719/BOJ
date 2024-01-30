import sys
input = sys.stdin.readline
n = int(input())
opinions = []
ans = 0
cnt = 0
if n == 0:
    print(0)
else:   
    for i in range(n):
        op = int(input())
        opinions.append(op)
    opinions.sort()
    cut = n*0.15
    if cut >= int(cut)+0.5:
        cut = int(cut)+1
    else:
        cut = int(cut)
    opinions = opinions[cut:n-cut]
    for i in opinions:
        ans += i
        cnt += 1
    ans /= cnt
    if ans >= int(ans)+0.5:
        ans = int(ans)+1
    else:
        ans = int(ans)
    print(ans)
