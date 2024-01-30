def hanoi(n, start, end):
    if n==1: #n=1이라면
        print(start, end) #목표 막대로 옮기기만 하면 끝
        return
    hanoi(n-1, start, 6-start-end)#n개의 탑을 옮길려면 n-1개를 목표 위치가 아닌 곳으로 이동
    print(start, end)#맨 밑에 있는 탑 목표하는 위치로 옮기기
    hanoi(n-1, 6-start-end, end) #목표하는 위치로 나머지 옮기기

n=int(input())
print(2**n-1) #횟수는 2의 n제곱에서 1을 뺀 것과 같음
hanoi(n, 1, 3)
