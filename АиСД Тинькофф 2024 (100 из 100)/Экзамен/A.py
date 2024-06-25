import sys


def get_test_time(one_time, in_unit, cd, sent):
    if sent % in_unit == 0:
        return (sent // in_unit) * (one_time * in_unit + cd) - cd
    return (sent // in_unit) * (one_time * in_unit + cd) + (sent % in_unit) * one_time


def get_test_num(one_time, in_unit, cd, time):
    calc = one_time * in_unit
    unit = (one_time * in_unit + cd)
    return (time // unit) * in_unit + min(time % unit, calc) // one_time


def can_test(devs, time, sent):
    s = 0
    tasks = []
    for d in devs:
        cur = get_test_num(*d, time)
        s += cur
        tasks.append(cur)
    return s >= sent, tasks


n, m = [int(x) for x in sys.stdin.readline().split()]
devs = [[int(x) for x in sys.stdin.readline().split()] for _ in range(m)]

mx = -1
for d in devs:
    mx = max(mx, get_test_time(*d, n))

l, r = 1, mx
t = float("inf")
res = None
while l <= r:
    mid = (l + r) // 2
    can, tasks = can_test(devs, mid, n)
    if can:
        t = min(t, mid)
        res = tasks
        r = mid - 1
    else:
        l = mid + 1

print(t)
print(*res)
