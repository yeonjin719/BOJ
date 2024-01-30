T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    cnt = 1
    candidate = list(map(int, input().split()))
    index = M
    if N == 1:
        print(1)
    else:
        findMax = candidate.copy()
        findMax.sort(reverse=True)
        maxNum = findMax[0]
        while True:
            if len(candidate) == 0:
                print("Error")
                break

            elif index == -1:
                index = len(candidate)-1

            if candidate[0] == maxNum:
                if index == 0:
                    print(cnt)
                    break
                else:
                    cnt += 1
                    candidate.pop(0)
                    findMax.pop(0)
                    maxNum = findMax[0]
                    index -= 1

            else:
                num = candidate[0]
                candidate.append(num)
                candidate.pop(0)
                index -= 1
