N = input()
d = {}
for i in list(map(int, input().split())):
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
M = input()
for j in list(map(int, input().split())):
    try:
        print(d[j], end =' ')
    except:
        print(0, end=' ')
