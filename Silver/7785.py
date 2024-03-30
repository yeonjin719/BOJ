N = int(input())
company = {}
answer = []
for i in range(N):
    name, info = input().split()
    if info == "enter":
        company[name] = 1
    else:
        company[name] = 0
    
for i in company.keys():
    if company[i] == 1:
        answer.append(i)

answer = sorted(answer, reverse=True)
for i in answer:
    print(i)
