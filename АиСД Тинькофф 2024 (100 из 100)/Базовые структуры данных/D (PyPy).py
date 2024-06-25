n = int(input())
balls = list(map(int,input().split()))

c = 0
stack = []

for i in range(len(balls)):
    if len(stack) == 0:
        stack.append((balls[i], 1))
        continue
    if stack[-1][0] == balls[i]:
        stack.append((balls[i], stack[-1][1]+1))
    elif stack[-1][1] >= 3:
        c += stack[-1][1]
        for _ in range(stack[-1][1]):
            stack.pop()
        if len(stack) == 0 or stack[-1][0] != balls[i]:
            stack.append((balls[i], 1))
            continue
        elif stack[-1][0] == balls[i]:
            stack.append((balls[i], stack[-1][1] + 1))
    else:
        stack.append((balls[i], 1))

while len(stack) > 0 and stack[-1][1] >= 3:
    c += stack[-1][1]
    for _ in range(stack[-1][1]):
        stack.pop()

print(c)