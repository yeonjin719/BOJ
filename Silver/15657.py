N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visited = [False]*N
def isRight(_num, _nums):
    if _num <= _nums:
        return True
    else:
        return False
    
def backtraking(num, _M):
    for i in range(N):
        if isRight(num, nums[i]):
            if _M >= 2:
                answer.append(nums[i])
                backtraking(nums[i], _M-1)
            if _M == 1:
                answer.append(nums[i])
                print(*answer)
                answer.pop(-1)
    answer.pop(-1)

for i in range(N):
    answer = []
    answer.append(nums[i])
    if M > 1:
        backtraking(nums[i], M-1)
    else:
        print(*answer)
