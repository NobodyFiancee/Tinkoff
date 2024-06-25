def largest_increasing_subsequence(a, n):
    prev = [-1] * n
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j]:
                if dp[i] - 1 < dp[j]:
                    prev[i] = j
                    dp[i] = dp[j] + 1

    last_index = 0
    length = dp[0]
    for i in range(1, n):
        if length < dp[i]:
            last_index = i
            length = dp[i]

    path = []
    while last_index >= 0:
        path.append(a[last_index])
        last_index = prev[last_index]

    return list(reversed(path)), length


n = int(input())
a = list(map(int, input().split()))

res, size = largest_increasing_subsequence(a, n)
print(size)
print(*res)