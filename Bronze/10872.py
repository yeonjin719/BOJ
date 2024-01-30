num=int(input())
answer=1
for i in range(num):
    answer=answer*(i+1) #i+1을 하는 이유는 i가 0부터 시작이기 때문 이 경우 0을 곱하기 때문에 답이 무조건 0만 나오는 불상사 생김
print(answer)
