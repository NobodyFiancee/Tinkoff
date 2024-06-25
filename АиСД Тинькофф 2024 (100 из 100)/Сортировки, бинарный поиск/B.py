n, k = map(int, input().split())
mas_sort = list(map(int, input().split()))
numbers = list(map(int, input().split()))

for i in range(k):
    l = 0
    r = n - 1
    while r - l > 1:
        mid = (l + r) // 2
        if numbers[i] == mas_sort[mid]:
            print(mas_sort[mid])
            break
        if numbers[i] > mas_sort[mid]:
            l = mid
        else:
            r = mid
    else:
        if numbers[i] - mas_sort[l] <= mas_sort[r] - numbers[i]:
            print(mas_sort[l])
        else:
            print(mas_sort[r])