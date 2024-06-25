a, b, c, d = list(map(int, input().split()))
l = -10**9
r = 10**9


def f(x):
    return a*x**3 + b*x**2 + c*x + d


while r - l > 10 ** -6:
    x = (l + r) / 2
    if f(l) * f(x) <= 0:
        r = x
    else:
        l = x

print("{:.4f}".format((l + r) / 2))