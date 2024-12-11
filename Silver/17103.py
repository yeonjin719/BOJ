def sieve(max_num):
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False 
    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False
    return is_prime

T = int(input())
results = []

for _ in range(T):
    N = int(input())
    is_prime = sieve(N)

    cnt = 0
    for a in range(2, (N // 2) + 1):
        b = N - a
        if is_prime[a] and is_prime[b]:
            cnt += 1
    results.append(cnt)

for result in results:
    print(result)
