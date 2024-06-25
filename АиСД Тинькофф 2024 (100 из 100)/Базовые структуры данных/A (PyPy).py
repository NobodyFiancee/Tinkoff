class Stack:
    def __init__(self):
        self.stack = []

    def push(self, obj):
        if len(self.stack) == 0:
            min_stack = obj
        else:
            min_stack = min(self.stack[-1][1], obj)
        self.stack.append((obj, min_stack))

    def pop(self):
        self.stack.pop()

    def minimum(self):
        return self.stack[-1][1]


stack = Stack()
n = int(input())

for i in range(n):
    inpt = list(map(int, input().split()))
    if inpt[0] == 1:
        stack.push(inpt[1])
    elif inpt[0] == 2:
        stack.pop()
    else:
        print(stack.minimum())