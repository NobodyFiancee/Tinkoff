n, k = map(int, input().split())
mas_sort = list(map(int, input().split()))
numbers = list(map(int, input().split()))

for i in range(k):
    l = 0
    r = n - 1
    while r - l >= 0:
        mid = (l + r) // 2
        if numbers[i] == mas_sort[mid]:
            print('YES')
            break
        if numbers[i] > mas_sort[mid]:
            l = mid + 1
        else:
            r = mid - 1
    else:
        print('NO')