import sys


class MaxHeap:
    def __init__(self, mas = []):
        self.heap = mas

    def _sift_down(self, n, i):
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        largest = i
        if left_child < n and self.heap[left_child] > self.heap[largest]:
            largest = left_child
        if right_child < n and self.heap[right_child] > self.heap[largest]:
            largest = right_child
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._sift_down(n, largest)

    def heapSort(self):
        n = len(self.heap)

        for i in range(n, -1, -1):
            self._sift_down(n, i)

        for i in range(n - 1, 0, -1):
            self.heap[i], self.heap[0] = self.heap[0], self.heap[i]
            self._sift_down(i, 0)


sys.setrecursionlimit(10 ** 8)
n = int(sys.stdin.readline())
heap = MaxHeap(list(map(int, sys.stdin.readline().split())))
heap.heapSort()
print(*heap.heap)