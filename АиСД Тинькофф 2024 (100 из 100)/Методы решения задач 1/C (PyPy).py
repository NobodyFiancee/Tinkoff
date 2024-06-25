def check(diff):
    cows = 1
    last = stalls[0]
    for x in stalls:
        if x - last >= diff:
            cows += 1
            last = x
    return cows >= count_cows


n, count_cows = map(int, input().split())
stalls = list(map(int, input().split()))
stalls.sort()

left = 0
right = stalls[-1] - stalls[0] + 1
while right - left > 1:
    mid = (right + left) // 2
    if check(mid):
        left = mid
    else:
        right = mid

print(left)