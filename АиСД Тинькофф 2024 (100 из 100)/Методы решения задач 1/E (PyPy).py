def check(nums, k, max_sum):
    count = 1
    current_sum = 0
    for num in nums:
        current_sum += num
        if current_sum > max_sum:
            count += 1
            current_sum = num
    return count <= k


def min_max_sum(nums, k):
    left = max(nums)
    right = sum(nums)

    while left < right:
        mid = (left + right) // 2
        if check(nums, k, mid):
            right = mid
        else:
            left = mid + 1

    return left


n, k = map(int, input().split())
nums = list(map(int, input().split()))

print(min_max_sum(nums, k))