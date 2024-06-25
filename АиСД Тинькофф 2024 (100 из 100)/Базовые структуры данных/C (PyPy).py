inp = list(input().split())
stack = []

for i in inp:
    if i.isdigit():
        stack.append(int(i))
    else:
        b, a = stack.pop(), stack.pop()
        if i == '+':
            stack.append(a + b)
        elif i == '-':
            stack.append(a - b)
        else:
            stack.append(a * b)

print(stack.pop())