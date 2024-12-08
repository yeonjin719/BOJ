def quadTree(_N, nums):
    if _N == 2:
        total = 0
        for i in range(_N):
            for j in range(_N):
                total += nums[i][j]
        if total == _N**2:
            return '1'
        elif total == 0: 
            return '0'
        else:
            return f"({nums[0][0]}{nums[0][1]}{nums[1][0]}{nums[1][1]})"
    else:
        total = 0
        for i in range(_N):
            for j in range(_N):
                total += nums[i][j]
        if total == _N**2: 
            return '1'
        elif total == 0: 
            return '0'
        else:
            nums1 = [row[:_N//2] for row in nums[:_N//2]]
            nums2 = [row[_N//2:] for row in nums[:_N//2]]
            nums3 = [row[:_N//2] for row in nums[_N//2:]]
            nums4 = [row[_N//2:] for row in nums[_N//2:]]
          
            return f"({quadTree(_N//2, nums1)}{quadTree(_N//2, nums2)}{quadTree(_N//2, nums3)}{quadTree(_N//2, nums4)})"


N = int(input())
nums = [list(map(int, input().strip())) for _ in range(N)]

answer = quadTree(N, nums)
print(answer)
