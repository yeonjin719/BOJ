T = int(input())

def solution():
    x1,y1,x2,y2 = map(int, input().split())
    n = int(input())
    cnt = 0
    for i in range(n):
        cx, cy, r = map(int, input().split())
        startINcircle = ((cx-x1)**2 + (cy-y1)**2) <= r**2
        endIncircle = ((cx-x2)**2 + (cy-y2)**2) <= r**2
        if startINcircle is True and endIncircle is False:
            cnt += 1
        elif startINcircle is False and endIncircle is True:
            cnt += 1
    return cnt

for i in range(T):
    print(solution())
