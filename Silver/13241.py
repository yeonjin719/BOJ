import sys
print = sys.stdout.write
A, B = map(int, input().split())
if A == B:
    print(str(A))
elif A == 1:
    print(str(B))
elif B == 1:
    print(str(A))
else:
    i = 2
    ans = 1
    while True:
        if i > A or i > B:
            break
        if A % i == 0 and B % i == 0:
            A = A // i
            B = B // i
            ans = ans * i
        else:
            i += 1
    ans = ans*A*B
    print(str(ans))
