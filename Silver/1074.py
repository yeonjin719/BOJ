import sys
sys.setrecursionlimit(10000) 
N, r, c = map(int, input().split())
cnt = 0
width = 2**N
answered = False
def SplitRec(startx, starty, width):
    global cnt
    if answered == True:
        return 0
    else:
        if width == 1: 
            if startx == c and starty == r:
                print(cnt)
                return 0
            cnt += 1
        if width >= 2:
            SplitRec(startx, starty, width//2)
            SplitRec(startx + width//2, starty, width//2)
            SplitRec(startx, starty + width//2, width//2)
            SplitRec(startx + width//2, starty + width//2, width//2)
        else:
            return 0

SplitRec(0,0,width)