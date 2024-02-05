from collections import deque

def dfs(graph, v, visitedDFS):
    visitedDFS[v-1] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visitedDFS[i-1]:
            dfs(graph, i, visitedDFS)

def bfs(graph, start, visitedBFS):
    queue = deque([start])
    visitedBFS[start-1] = True
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visitedBFS[i-1]:
                queue.append(i)
                visitedBFS[i-1] = True

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
    
visitedDFS = [False] * N
visitedBFS = [False] * N

dfs(graph, V, visitedDFS)
print()  
bfs(graph, V, visitedBFS)
