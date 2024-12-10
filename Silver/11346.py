n = int(input())

def answer(N, M):
  name = list(input().split())
  name2= list(input().split())
  name = name + name2
  name = set(name)
  return len(name);

for i in range(n):
  input()
  N, M = map(int, input().split())
  print(answer(N, M))
  