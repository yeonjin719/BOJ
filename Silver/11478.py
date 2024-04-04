n = str(input())
candidate = []
for i in range(len(n)):
    for j in range(i, len(n)):
        candidate.append(n[i:j+1])
candidate = set(candidate)
print(len(candidate))
