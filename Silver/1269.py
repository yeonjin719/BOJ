import sys
print = sys.stdout.write
input = sys.stdin.readline

Anum, Bnum = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

answer = len(A^B)
print(str(answer))
