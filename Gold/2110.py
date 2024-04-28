N, C = map(int, input().split())
where = []
for i in range(N):
    where.append(int(input()))

where.sort()

start = 1
end = where[-1]-where[0]
result = 0

while (start <= end):
    mid = (start+end)//2
    value = where[0]
    cnt = 1
    for i in range(1, N):
        if where[i] >= value+mid:
            value = where[i]
            cnt += 1
    if cnt >= C:
        start = mid +1
        result = mid
    else:
        end = mid - 1

print(result)
