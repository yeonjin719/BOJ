import sys
input = sys.stdin.readline

def row(n, x):
    for i in range(9):
        if sudoku[x][i] == n:
            return False
    return True

def col(n, y):
    for i in range(9):
        if sudoku[i][y] == n:
            return False
    return True

def rect(x, y ,n):
    nx = x//3*3
    ny = y//3*3
    for l in range(3):
        for k in range(3):
           if sudoku[nx + l][ny + k] == n:
               return False
    return True

def findNum(cnt):    
    if cnt == len(blank):
        for i in range(9):
            print(*sudoku[i])
        exit()
    x = blank[cnt][0]
    y = blank[cnt][1]
    for i in range(1, 10):
        if col(i, y) and row(i,x) and rect(x,y,i):
            sudoku[x][y] = i
            findNum(cnt+1)
            sudoku[x][y] = 0

sudoku = [list(map(int, input().split())) for _ in range(9)]

blank = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append([i, j])

findNum(0)
