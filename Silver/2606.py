import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().rstrip())
K = int(input().rstrip())
answer = [0 for _ in range(N)]
visited = [0 for _ in range(N)]

graph = {}

def find(graph_list, visited):
    for i in graph_list:
        if visited[i-1] == 1:
            continue
        else:
            answer[i-1] = 1
            visited[i-1] = 1
            find(graph[i], visited)
            
    return answer

for i in range(N):
    graph[i+1] = []

for i in range(K):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

find(graph[1], visited)

print(str(sum(answer[1:])))
