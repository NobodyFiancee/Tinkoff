from collections import deque

n, k = map(int, input().split())
coins = [0] + list(map(int, input().split())) + [0]
n -= 1
dp = [0] * (n + 1)
prev_stolbik = [0] * (n + 1)
max_coins = float('-inf')

deque_max = deque([0])
for i in range(1, n + 1):
    while deque_max and deque_max[0] < i - k:
        deque_max.popleft()

    max_index = deque_max[0]
    max_value = dp[max_index] + coins[i]

    dp[i] = max_value
    prev_stolbik[i] = max_index

    while deque_max and dp[i] >= dp[deque_max[-1]]:
        deque_max.pop()
    deque_max.append(i)

path = []
current_stolbik = n
while current_stolbik != 0:
    path.append(current_stolbik)
    current_stolbik = prev_stolbik[current_stolbik]
path.append(0)

path.reverse()

print(dp[n])
print(len(path) - 1)
print(" ".join(str(x + 1) for x in path))