from collections import deque


class QueueMP:
    def __init__(self):
        self.left = deque()
        self.right = deque()

    def push(self, value):
        self.left.appendleft(value)

    def middle_push(self, value):
        while len(self.right) < len(self.left):
            self.right.appendleft(self.left.pop())
        self.left.append(value)

    def pop(self):
        while len(self.right) < len(self.left):
            self.right.appendleft(self.left.pop())
        print(self.right.pop())


q = QueueMP()
n = int(input())
for _ in range(n):
    inpt = input().split()
    if inpt[0] == '+':
        q.push(inpt[1])
    elif inpt[0] == '-':
        q.pop()
    elif inpt[0] == '*':
        q.middle_push(inpt[1])