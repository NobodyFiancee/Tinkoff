import sys


def query(x):
    print(x)
    sys.stdout.flush()
    return input()


n = int(input())
l = 1
r = n + 1
mid = n // 2
while r - l > 1:
    if query(mid) == '>=':
        l = mid
    else:
        r = mid
    mid = (l+r)//2
print(f'! {l}')