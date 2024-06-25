def build_segment_tree(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = (start + end) // 2
        build_segment_tree(arr, tree, 2 * node + 1, start, mid)
        build_segment_tree(arr, tree, 2 * node + 2, mid + 1, end)
        tree[node] = tree[2 * node + 1] + tree[2 * node + 2]


def update_tree(arr, tree, node, start, end, idx):
    if start == end:
        arr[idx] = 1 - arr[idx]
        tree[node] = arr[idx]
    else:
        mid = (start + end) // 2
        if start <= idx <= mid:
            update_tree(arr, tree, 2 * node + 1, start, mid, idx)
        else:
            update_tree(arr, tree, 2 * node + 2, mid + 1, end, idx)
        tree[node] = tree[2 * node + 1] + tree[2 * node + 2]


def find_kth_one(tree, node, start, end, k):
    if tree[node] < k:
        return -1
    if start == end:
        return start
    mid = (start + end) // 2
    if tree[2 * node + 1] >= k:
        return find_kth_one(tree, 2 * node + 1, start, mid, k)
    else:
        return find_kth_one(tree, 2 * node + 2, mid + 1, end, k - tree[2 * node + 1])


n, m = map(int, input().split())
arr = list(map(int, input().split()))

tree = [0] * (4 * n)
build_segment_tree(arr, tree, 0, 0, n - 1)

for _ in range(m):
    op, arg = map(int, input().split())
    if op == 1:
        update_tree(arr, tree, 0, 0, n - 1, arg)
    elif op == 2:
        print(find_kth_one(tree, 0, 0, n - 1, arg + 1))