N, K = map(int, input().split())
target = []
for i in range(N):
  a, b = map(int, input().split())
  target.append([a, b, i+1])

target.sort(key=lambda x:x[0], reverse=True)
target = target[0:K]


target.sort(key=lambda x:x[1], reverse=True)

print(target[0][2])