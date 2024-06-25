n = int(input())
res = []
for i in range(1, n+1):
    res.append(i)

for i in range(n):
    res[i], res[i//2] = res[i//2], res[i]

print(' '.join(map(str, res)))