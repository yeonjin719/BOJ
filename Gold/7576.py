from collections import deque
import sys
import copy
input = sys.stdin.readline
M, N = map(int, input().split())
tomatoes = deque()
for i in range(N):
    tomatoes.append(list(map(int, input().split())))
ans = 0
startPoint = deque()

for i in range(N):
	for j in range(M):
		if tomatoes[i][j] == 1:
			startPoint.append([i, j])

def bfs(tomatoes, x, y, queue):
	global changed
	calXY = [[-1, 0],[0, -1],[1, 0], [0, 1]]
	for k, l in calXY:
		if x+k >= 0 and x+k <= N-1 and y+l >=0 and y+l <= M-1:
			if tomatoes[x+k][y+l] == 0:
				tomatoes[x+k][y+l] = 1
				queue.append([x+k, y+l])
				changed = True
	return changed

while True:
	changed = False
	queue = deque()
	while startPoint:
		i, j = startPoint.popleft()
		bfs(tomatoes, i, j, queue)
	if changed == False:
		break
	else:
		ans += 1
		startPoint = copy.deepcopy(queue)

isAllChanged = True
for i in range(N):
	for j in range(M):
		if tomatoes[i][j] == 0:
			isAllChanged = False
			break

if isAllChanged == False:
	print(-1)
else:
	print(ans)
