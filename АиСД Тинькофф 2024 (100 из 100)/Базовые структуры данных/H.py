def get_nearest_smaller_by_index(arr, start, end, step):
    n = len(arr)
    stack = []
    boundaries = [-1] * n
    for i in range(start, end, step):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            boundaries[i] = stack[-1]
        stack.append(i)
    return boundaries


def max_subsection(arr):
    n = len(arr)
    left_boundaries = get_nearest_smaller_by_index(arr, 0, n, 1)
    right_boundaries = get_nearest_smaller_by_index(arr, n - 1, -1, -1)

    pref_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        pref_sum[i] = pref_sum[i - 1] + arr[i - 1]

    res = 0
    for i in range(n):
        left = left_boundaries[i] + 1
        right = right_boundaries[i] - 1 if right_boundaries[i] != -1 else n - 1
        res = max(res, arr[i] * (pref_sum[right + 1] - pref_sum[left] if left <= right else 0))

    return res


n = int(input())
arr = list(map(int, input().split()))
print(max_subsection(arr))