L = int(input())
alpha = list(str(input()))
answer = 0
for i in range(L):
    num =ord(alpha[i])
    answer += (ord(alpha[i])-96)*(31**i)

print(answer%1234567891)
