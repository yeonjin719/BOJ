a,b,c = map(int, input().split())

def fpow(a, b, c):
    if b == 1:
        return a%c
    elif b == 2:
        return (a*a)%c
    else:
        if b%2:
            return ((fpow(a,b//2,c)**2)*a)%c
        else:
            return ((fpow(a,b//2,c)**2))%c
        
print(fpow(a,b,c))
