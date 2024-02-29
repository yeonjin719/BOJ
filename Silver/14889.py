import copy
N = int(input())
ability = []
for i in range(N):
    ability.append(list(map(int, input().split())))
targets = []

def choose(num, N, ans):
    global targets
    for i in range(N):
        if i <= num:
            pass
        else:
            ans.append(i)
            if len(ans) < N//2:
                choose(i, N, ans)
            else:
                targets.append(copy.deepcopy(ans))
            ans.pop()

def countAbility(target1, target2):
    global MinAbilityGap, ansMinTeam, start, link
    for i in target1:
        for j in target1:
            start += ability[i][j]
    
    for k in target2:
        for l in target2:
            link += ability[k][l]

    if start-link < 0:
        if (start-link)*-1 < MinAbilityGap:
            MinAbilityGap = (start-link)*-1
            ansMinTeam = target1
    else:
        if (start-link) < MinAbilityGap:
            MinAbilityGap = (start-link)
            ansMinTeam = target1
    return MinAbilityGap



ans = []
choose(-1, N, ans)
MinAbilityGap = 987654321
ansMinTeam = []
start = 0
link = 0
MinLink = 10000000
MinStart = 10000000
for i in range(len(targets)//2):
    start = 0
    link = 0
    countAbility(targets[i], targets[len(targets)-1-i])

print(MinAbilityGap)
