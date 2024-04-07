import sys
input = sys.stdin.readline
n = int(input())
x = []
for i in range(n):
    x.append(int(input()))

length = []

for i in range(n-1):
    length.append(x[i+1]-x[i])

minlength = min(length)
Banswer = 1
if minlength != 1:
    for i in range(2, minlength+1):
        for j in range(n-1):
            if length[j] % i != 0:
                break
        else:
            Banswer = i
answer = 0

for i in length:
    answer += (i//Banswer)-1

print(answer)
