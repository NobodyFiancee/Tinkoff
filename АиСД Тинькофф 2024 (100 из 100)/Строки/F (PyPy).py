def manacher(s):
    s = '#' + '#'.join(s) + '#'
    n = len(s)
    d = [0] * n
    l, r = 0, -1
    res = 0

    for i in range(n):
        k = 0
        if i <= r:
            k = min(d[l + r - i], r - i)
        while 0 <= i - k - 1 and i + k + 1 < n and s[i - k - 1] == s[i + k + 1]:
            k += 1
        d[i] = k
        if i + k > r:
            l, r = i - k, i + k
        res += (k + 1) // 2
    return res


s = input()
print(manacher(s))