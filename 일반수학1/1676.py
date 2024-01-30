N = int(input())
cnt = 0
ans = 1
for i in range(N, 1, -1):
    ans *= i

while True:
    if ans % 5 != 0:
        break
    ans //= 5
    cnt += 1
print(cnt)
