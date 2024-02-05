from collections import deque
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
answer = []
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

def bfs(graph, start):
    num = [0]*(N+1)
    visited = [start]
    queue = deque()
    queue.append(start)
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if i not in visited:
                num[i] = num[v]+1
                visited.append(i)
                queue.append(i)
    return sum(num)


for i in range(1, N+1):
    answer.append(bfs(graph, i))

print(answer.index(min(answer))+1)
