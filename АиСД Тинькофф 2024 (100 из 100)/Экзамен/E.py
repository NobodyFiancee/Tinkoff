class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.lazy = [0] * (4 * size)
        self.tree = [0] * (4 * size)

    def build(self, start, end, node, array):
        if start == end:
            self.tree[node] = array[start]
        else:
            mid = (start + end) // 2
            self.build(start, mid, 2 * node + 1, array)
            self.build(mid + 1, end, 2 * node + 2, array)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update_range(self, start, end, left, right, node):
        if self.lazy[node] != 0:
            self.tree[node] = (end - start + 1) - self.tree[node]
            if start != end:
                self.lazy[2 * node + 1] ^= 1
                self.lazy[2 * node + 2] ^= 1
            self.lazy[node] = 0

        if start > end or start > right or end < left:
            return

        if start >= left and end <= right:
            self.tree[node] = (end - start + 1) - self.tree[node]
            if start != end:
                self.lazy[2 * node + 1] ^= 1
                self.lazy[2 * node + 2] ^= 1
            return

        mid = (start + end) // 2
        self.update_range(start, mid, left, right, 2 * node + 1)
        self.update_range(mid + 1, end, left, right, 2 * node + 2)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query_range(self, start, end, left, right, node):
        if self.lazy[node] != 0:
            self.tree[node] = (end - start + 1) - self.tree[node]
            if start != end:
                self.lazy[2 * node + 1] ^= 1
                self.lazy[2 * node + 2] ^= 1
            self.lazy[node] = 0

        if start > end or start > right or end < left:
            return 0

        if start >= left and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        left_query = self.query_range(start, mid, left, right, 2 * node + 1)
        right_query = self.query_range(mid + 1, end, left, right, 2 * node + 2)
        return left_query + right_query

size = int(input())
array = list(map(int, input().split()))

query_count = int(input())
queries = [list(map(int, input().split())) for _ in range(query_count)]

segment_trees = [SegmentTree(size) for _ in range(20)]
for i in range(20):
    binary_array = [(array[j] >> i) & 1 for j in range(size)]
    segment_trees[i].build(0, size - 1, 0, binary_array)

results = []

for query in queries:
    if query[0] == 1:
        left, right = query[1] - 1, query[2] - 1
        total_sum = 0
        for i in range(20):
            bit_count = segment_trees[i].query_range(0, size - 1, left, right, 0)
            total_sum += bit_count * (1 << i)
        results.append(total_sum)
    elif query[0] == 2:
        left, right, value = query[1] - 1, query[2] - 1, query[3]
        for i in range(20):
            if (value >> i) & 1:
                segment_trees[i].update_range(0, size - 1, left, right, 0)

for result in results:
    print(result)
