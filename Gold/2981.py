import sys
input = sys.stdin.readline
re_num = []
N = int(input())
num = sorted([int(input()) for _ in range(N)])

for i in range(1, N):
    re_num.append(num[i]-num[i-1])

def findGCD(a, b):
    num = b
    div = a
    rest = num % div
    while rest != 0:
        num = div
        div = rest
        rest = num % div
    return div

GCD = re_num[0]
for idx in range(1, len(re_num)):
    GCD = findGCD(GCD, re_num[idx])

result = set()
for i in range(2, int(GCD**0.5)+1):
    if GCD % i == 0:
        result.add(i)
        result.add(GCD//i)
result.add(GCD)
print(*sorted(list(result)))
