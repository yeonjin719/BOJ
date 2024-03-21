def cantor(n, blank):
    if blank == True:
        print(" "*n, end='')
        return 0
    if n == 1:
        print("-", end='')
        return 0
    else:
        cantor(n//3, False)
        cantor(n//3, True)
        cantor(n//3, False)

def solution():
    while True:
        try:
            N = int(input())
            cantor(3**N, False)
            print()
        except:
            break

solution()
