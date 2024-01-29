import sys

white = 0
blue = 0

def calculateSum(total_list):
    return sum(map(lambda x: sum(x), total_list))

def splitPaper(total_list, N):
    global white, blue

    if N == 2:
        if calculateSum(total_list) == 0:
            white += 1
        elif calculateSum(total_list) == 1:
            white += 3
            blue += 1
        elif calculateSum(total_list) == 2:
            white += 2
            blue += 2
        elif calculateSum(total_list) == 3:
            white += 1
            blue += 3
        else:
            blue += 1
    
    else:
        nextN = N // 2
        paper1 = list(map(lambda x:x[:nextN], total_list[:nextN]))
        paper2 = list(map(lambda x:x[nextN:], total_list[:nextN]))
        paper3 = list(map(lambda x:x[:nextN], total_list[nextN:]))
        paper4 = list(map(lambda x:x[nextN:], total_list[nextN:]))
        for newPaper in [paper1, paper2, paper3, paper4]:
            if calculateSum(newPaper) == 0:
                white += 1
            elif calculateSum(newPaper) == nextN**2:
                blue += 1
            else:
                splitPaper(newPaper, nextN)

N = int(input())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
if calculateSum(paper) == 0:
    white += 1
    print(white)
    print(blue)
elif calculateSum(paper) == N**2:
    blue += 1
    print(white)
    print(blue)
else:
    splitPaper(paper, N)
    print(white)
    print(blue)
