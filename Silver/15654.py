def dfs(nums, current, visited, cnt, M):
    if cnt == M:
        print(" ".join(map(str, current)))
        return
    
    for i in range(len(nums)):
        if not visited[i]:
            visited[i] = True
            dfs(nums, current + [nums[i]], visited, cnt + 1, M)
            visited[i] = False

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visited = [False] * N
dfs(nums, [], visited, 0, M)
