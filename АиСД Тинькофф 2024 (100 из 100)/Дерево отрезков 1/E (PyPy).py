class SegmentTree:
    def __init__(self, nums):
        self.size = 4 * len(nums)
        self.tree = [(0, 1)] * self.size
        self.arr = [0] * len(nums)
        sorted_arr = sorted((val, -idx) for idx, val in enumerate(nums))
        for _, i in sorted_arr:
            m = self.get_max(0, 0, len(nums) - 1, 0, -i)
            self.change(-i, m[0] + 1, m[1])

    def get_max(self, node, start, end, left, right):
        if left > end or right < start:
            return (0, 1)
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        left_max = self.get_max(left_child, start, mid, left, right)
        right_max = self.get_max(right_child, mid + 1, end, left, right)
        if left_max[0] > right_max[0]:
            return left_max
        elif left_max[0] < right_max[0]:
            return right_max
        elif left_max[0] == 0:
            return (0, 1)
        else:
            return (left_max[0], (left_max[1] + right_max[1]) % MOD)

    def change(self, idx, num, cnt):
        self._change(0, 0, len(self.arr) - 1, idx, num, cnt)

    def _change(self, node, start, end, idx, num, cnt):
        if start == end:
            self.arr[idx] = num
            self.tree[node] = (num, cnt)
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            if start <= idx <= mid:
                self._change(left_child, start, mid, idx, num, cnt)
            else:
                self._change(right_child, mid + 1, end, idx, num, cnt)
            if self.tree[left_child][0] > self.tree[right_child][0]:
                self.tree[node] = self.tree[left_child]
            elif self.tree[left_child][0] < self.tree[right_child][0]:
                self.tree[node] = self.tree[right_child]
            else:
                self.tree[node] = (self.tree[right_child][0], (self.tree[left_child][1] + self.tree[right_child][1]) % MOD)

    def result(self):
        return self.tree[0][1]


MOD = 10**9 + 7
n = int(input())
nums = list(map(int, input().split()))
seg_tree = SegmentTree(nums)
print(seg_tree.result())