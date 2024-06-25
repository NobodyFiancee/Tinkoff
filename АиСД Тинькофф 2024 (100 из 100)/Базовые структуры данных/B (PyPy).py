from collections import deque

n, k = map(int, input().split())
mas = list(map(int, input().split()))
res = []

dek = deque()
for i in range(n):
    while len(dek) > 0 and dek[0] < i - k + 1:
        dek.popleft()
    while len(dek) > 0 and mas[dek[-1]] > mas[i]:
        dek.pop()
    dek.append(i)

    if i >= k - 1:
        res.append(mas[dek[0]])

print(*res)