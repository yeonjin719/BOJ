N, K = map(int, input().split())
L = []
index = K-1
for i in range(N):
    L.append(i+1)
print("<", end='')
for i in range(N):
    print(L[index], end ='')
    L.pop(index)
    index += K
    if index > len(L)-1:
        if len(L) == 0:
            index = 0
        else:
            index %= len(L)
            index -= 1
            if index < 0:
                index = len(L)-1
    else:
        index -= 1
    if i<N-1:
        print(", ", end ='')
print(">")
