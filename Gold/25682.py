import copy
N, M, K = map(int, input().split())
arr = [[0]*(M+1)]

def count(_arr, color):
    for i in range(1, N+1):
        for j in range(1, M+1):
            if (i+j)%2 == 0:
                if _arr[i][j] != color:
                    _arr[i][j] = 1 + _arr[i-1][j] + _arr[i][j-1] - _arr[i-1][j-1]
                else:
                    _arr[i][j] = _arr[i-1][j] + _arr[i][j-1] - _arr[i-1][j-1]
            else:
                if _arr[i][j] != color:
                    _arr[i][j] = _arr[i-1][j] + _arr[i][j-1] - _arr[i-1][j-1]
                else:
                    _arr[i][j] = 1 + _arr[i-1][j] + _arr[i][j-1] - _arr[i-1][j-1]

    return _arr

def splitMatrix(K):
    if K == N and K == M:
        startPointX = [1]
        startPointY = [1]
    elif K == M and K != N:
        startPointX = [i+1 for i in range(N-K+1)]
        startPointY = [1]
    elif K == N and K != M:
        startPointX = [1]
        startPointY = [i+1 for i in range(M-K+1)]
    else:
        startPointX = [i+1 for i in range(N-K+1)]
        startPointY = [i+1 for i in range(M-K+1)]
    return startPointX, startPointY

for i in range(N):
    arr.append([0]+list(input()))


N1arr = count(copy.deepcopy(arr), "B")

ans = 987654321
X, Y= (splitMatrix(K))
for x in X:
    for y in Y:
        num = N1arr[x+K-1][y+K-1] - N1arr[x-1][y+K-1] - N1arr[x+K-1][y-1] + N1arr[x-1][y-1]
        if num < ans:
            ans = num

N2arr = count(copy.deepcopy(arr), "W")

X, Y= (splitMatrix(K))
for x in X:
    for y in Y:
        num = N2arr[x+K-1][y+K-1] - N2arr[x-1][y+K-1] - N2arr[x+K-1][y-1] + N2arr[x-1][y-1]
        if num < ans:
            ans = num
print(ans)
