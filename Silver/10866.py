from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
a = deque()
len = 0
answer = []
for i in range(N):
    order = input().strip()
    if order == "size":
        answer.append(len)
    elif order == "empty":
        if len == 0:
            answer.append(1)
        else:
            answer.append(0)
    elif order == "front":
        if len == 0:
            answer.append(-1)
        else:
            answer.append(a[0])
    elif order == "back":
        if len == 0:
            answer.append(-1)
        else:
            answer.append(a[-1])
    else:
        order, direction = order.split('_')
        if order == "pop":
            if direction == "front":
                if len == 0:
                    answer.append(-1)
                else:
                    answer.append(a[0])
                    a.popleft()
                    len -= 1
            else:
                if len == 0:
                    answer.append(-1)
                else:
                    answer.append(a[-1])
                    a.pop()
                    len -= 1
        else: 
            len += 1
            direction, num = direction.split() 
            if direction == "front":
                a.appendleft(num)
            else:
                a.append(num)
for i in answer:
    print(i)
