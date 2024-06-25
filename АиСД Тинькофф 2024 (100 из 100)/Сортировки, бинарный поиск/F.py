def merge_sort(mas):
    if len(mas) < 2:
        return mas[:]
    mid = len(mas) // 2
    left = merge_sort(mas[:mid])
    right = merge_sort(mas[mid:])
    return merge(left, right)


def merge(l, r):
    global merged
    res = []
    i, j = 0, 0
    while i < len(l) and j < len(r):
        if l[i]<=r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1
            merged += len(l) - i
    while i < len(l):
        res.append(l[i])
        i += 1
    while j < len(r):
        res.append(r[j])
        j += 1
    return res


merged = 0
n = int(input())
mas = list(map(int, input().split()))
res = merge_sort(mas)
print(merged)
print(' '.join(map(str, res)))