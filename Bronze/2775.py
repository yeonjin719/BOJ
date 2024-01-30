T=int(input())
for i in range(T):
    a=int(input())
    b=int(input())
    people=[]
    for j in range(b): #0층에 사는 사람 리스트를 만든다
        people.append(j+1)
    for k in range(a): #a층만큼 반복
        for l in range(b):#b호만큼 반복
            if l==0: #1호(0번째 호)는 무조건 1명이므로 넘어간다
                pass
            else:
                people[l]=sum(people[l-1:l+1]) #l번째 호에 사는 사람은 l-1호부터 l호에 사는 사람 수를 더한 것
    print(people[b-1]) #b호에 사는 사람은 b-1번째 호이므로 b-1번째를 출력
