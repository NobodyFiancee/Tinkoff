import sys


class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [None] * (4 * len(arr))
        self.build(0, 0, len(arr) - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = start
        else:
            mid = (start + end) // 2
            self.build(2 * node + 1, start, mid)
            self.build(2 * node + 2, mid + 1, end)
            left_min_index = self.tree[2 * node + 1]
            right_min_index = self.tree[2 * node + 2]
            if self.arr[left_min_index] <= self.arr[right_min_index]:
                self.tree[node] = left_min_index
            else:
                self.tree[node] = right_min_index

    def query_min_index(self, node, start, end, x, l):
        if start == l and end < l:
            return -1

        if start == end:
            if self.arr[start] >= x:
                return start
            else:
                return -1

        mid = (start + end) // 2
        if l <= mid:
            left_result = self.query_min_index(2 * node + 1, start, mid, x, l)
            if left_result != -1:
                return left_result
        return self.query_min_index(2 * node + 2, mid + 1, end, x, l)

    def update(self, node, start, end, index, value):
        if start == end == index:
            self.arr[index] = value
        else:
            mid = (start + end) // 2
            if index <= mid:
                self.update(2 * node + 1, start, mid, index, value)
            else:
                self.update(2 * node + 2, mid + 1, end, index, value)

            left_min_index = self.tree[2 * node + 1]
            right_min_index = self.tree[2 * node + 2]
            if self.arr[left_min_index] <= self.arr[right_min_index]:
                self.tree[node] = left_min_index
            else:
                self.tree[node] = right_min_index


sys.setrecursionlimit(10**7)
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

seg_tree = SegmentTree(arr)

for _ in range(m):
    query_type, *args = map(int, sys.stdin.readline().split())
    if query_type == 1:
        i, v = args
        seg_tree.update(0, 0, n - 1, i, v)
    elif query_type == 2:
        x, l = args
        result = seg_tree.query_min_index(0, 0, n - 1, x, l)
        sys.stdout.write(str(result) + '\n')

