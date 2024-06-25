import sys


class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, x):
        self.heap.append(x)
        self._sift_up(len(self.heap) - 1)

    def extract(self):
        if len(self.heap) == 0:
            return None
        max_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self._sift_down(0)
        return max_val

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[parent] < self.heap[i]:
                self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
                i = parent
            else:
                break

    def _sift_down(self, i):
        n = len(self.heap)
        while i < n:
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            largest = i
            if left_child < n and self.heap[left_child] > self.heap[largest]:
                largest = left_child
            if right_child < n and self.heap[right_child] > self.heap[largest]:
                largest = right_child
            if largest != i:
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                i = largest
            else:
                break


n = int(input())
commands = [sys.stdin.readline().split() for _ in range(n)]

heap = MaxHeap()

for command in commands:
    if command[0] == '0':
        heap.insert(int(command[1]))
    elif command[0] == '1':
        print(heap.extract())