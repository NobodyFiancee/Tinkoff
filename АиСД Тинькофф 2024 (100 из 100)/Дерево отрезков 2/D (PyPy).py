import sys

def propagate_updates(segment_tree, lazy_updates, node_index, node_left, node_right):
    segment_tree[node_index] += lazy_updates[node_index]
    if node_left < node_right - 1:
        lazy_updates[node_index * 2] += lazy_updates[node_index]
        lazy_updates[node_index * 2 + 1] += lazy_updates[node_index]
    lazy_updates[node_index] = 0

def update_segment_tree(segment_tree, left_bound, right_bound, value, ys, lazy_updates, n):
    stack = [[1, -1, 0, n]]

    while stack:
        stack[-1][1] += 1
        node_index, state, node_left, node_right = stack[-1]
        propagate_updates(segment_tree, lazy_updates, node_index, node_left, node_right)

        if node_left >= left_bound and node_right <= right_bound:
            lazy_updates[node_index] += value
            if ys[node_index] == n - 1:
                ys[node_index] = node_right - 1
            propagate_updates(segment_tree, lazy_updates, node_index, node_left, node_right)
            stack.pop()
            continue
        if node_right <= left_bound or node_left >= right_bound:
            stack.pop()
            continue
        mid = (node_left + node_right) // 2
        if state == 0:
            stack.append([node_index * 2, -1, node_left, mid])
        elif state == 1:
            stack.append([node_index * 2 + 1, -1, mid, node_right])
        else:
            stack.pop()
            if segment_tree[node_index * 2] > segment_tree[node_index * 2 + 1]:
                segment_tree[node_index] = segment_tree[node_index * 2]
                ys[node_index] = ys[node_index * 2]
            else:
                segment_tree[node_index] = segment_tree[node_index * 2 + 1]
                ys[node_index] = ys[node_index * 2 + 1]


n = int(sys.stdin.readline())

queries = [None] * n * 2
rectangles = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
for i in range(0, n * 2, 2):
    x1, y1, x2, y2 = rectangles[i // 2]
    queries[i] = [x1, 0, y1, y2]
    queries[i + 1] = [x2, 1, y1, y2]
queries.sort()

coordinate_range = 2 * 10 ** 5
tree_size = coordinate_range * 2 + 1
segment_tree = [0] * 4 * tree_size
ys = [tree_size - 1] * 4 * tree_size
lazy_updates = [0] * 4 * tree_size

max_rects = 0
coords = None
for query in queries:
    add = 1 if query[1] == 0 else -1
    update_segment_tree(segment_tree, query[2] + coordinate_range, query[3] + coordinate_range + 1, add, ys, lazy_updates, tree_size)
    if segment_tree[1] > max_rects:
        max_rects = segment_tree[1]
        coords = query[0], ys[1] - coordinate_range

print(max_rects)
print(*coords)