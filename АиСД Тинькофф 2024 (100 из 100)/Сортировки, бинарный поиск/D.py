import math

c = float(input())
l = -1
r = c

while r - l > 10 ** -6:
    x = (l + r) / 2
    if x ** 2 + math.sqrt(x + 1) < c:
        l = x
    else:
        r = x

print(round(x, 6))