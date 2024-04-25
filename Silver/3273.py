import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
nums = sorted(nums)
target = int(input())
cnt = 0
invert_sum = 0
for i in range(n):
    end = i+1
    invert_sum = nums[i]
    while invert_sum < target and end < n:
        invert_sum += nums[end]
        if invert_sum == target:
            cnt += 1
        elif invert_sum > target:
            break
        invert_sum -= nums[end]
        end += 1

print(cnt)
