A, B, V = map(int, input().split())
D = 0
D += (V-B)/(A-B) #A*D-B*(D-1)=V를 전개
if D==int(D):
    print(int(D))
else:
    print(int(D)+1) #소수가 나오는 경우 결국 하루를 더 사용하는 것이기 때문에 +1