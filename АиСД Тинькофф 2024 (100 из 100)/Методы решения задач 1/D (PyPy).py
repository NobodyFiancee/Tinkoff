n, k = map(int, input().split())
left = 1
right = n * n + 1

while right - left > 1:
    mid = (right + left) // 2
    ans = 0
    for i in range(1, n + 1):
        ans += min(n, (mid - 1) // i)
    if ans < k:
        left = mid
    else:
        right = mid

print(left)