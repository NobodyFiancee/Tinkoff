def calculate_sum(n, m, k, is_vertical):
    if is_vertical:
        return ((((1 + k) / 2) * k + (((m * (n - 1) + 1) + (m * (n - 1) + k)) / 2) * k) / 2) * n
    else:
        return ((1 + m * k) / 2) * m * k


def find_best_cut(n, m):
    target_sum = ((1 + n * m) / 4) * n * m
    best_diff = float('inf')
    best_cut = ('V', 1)

    def binary_search(low, high, is_vertical):
        nonlocal best_diff
        nonlocal best_cut
        while low <= high:
            mid = (low + high) // 2
            current_sum = calculate_sum(n, m, mid, is_vertical)
            diff = abs(current_sum - target_sum)

            if diff < best_diff:
                best_diff = diff
                best_cut = ('V' if is_vertical else 'H', mid)

            if current_sum < target_sum:
                low = mid + 1
            else:
                high = mid - 1

    binary_search(0, m+n+1, False)
    binary_search(0, m+n+1, True)

    return best_cut


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    cut_type, cut_position = find_best_cut(n, m)
    print(f"{cut_type} {cut_position+1}")