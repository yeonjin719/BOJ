K, N = map(int, input().split())
Lenlength = []
for i in range(K):
    Lenlength.append(int(input()))

cnt = 0
minlength = 0
maxlength =  max(Lenlength)
middlelength = max(Lenlength)//2
while True:
    cnt = 0
    for i in Lenlength:
        if middlelength == 0:
            cnt += i//maxlength
        else:
            cnt += i//(((maxlength+minlength)//2))
    if cnt < N:
        maxlength = ((maxlength+minlength)//2)
        #print("cnt가 N보다 작을 때",cnt, maxlength, (((maxlength+minlength)//2)), minlength)
    else:
        minlength = ((maxlength+minlength)//2)
        #print("cnt가 N보다 클 때",cnt, maxlength, (((maxlength+minlength)//2)), minlength)
        if maxlength-minlength <= 2:
            cnt = 0
            for i in Lenlength:
                cnt += i//maxlength
            if cnt >= N:
                print(maxlength)
            else:
                cnt = 0
                for i in Lenlength:
                    cnt += i//((maxlength+minlength)//2)
                if cnt >= N:
                    print(((maxlength+minlength)//2))
                else:
                    print(minlength)
            break
