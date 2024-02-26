import sys
input = sys.stdin.readline

sentence = input().rstrip()
N = int(input())
cnt = [[0]*26]
cnt[0][ord(sentence[0])-97]=1

for i in range(1, len(sentence)):
    cnt.append(cnt[-1][:])
    cnt[i][ord(sentence[i])-97]+=1
    

for i in range(N):
    alphabet, l, r = input().split()
    if int(l) == 0:
        print(cnt[int(r)][ord(alphabet)-97])
    else:
        print(cnt[int(r)][ord(alphabet)-97]-cnt[int(l)-1][ord(alphabet)-97])
