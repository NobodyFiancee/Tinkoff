from collections import deque


def is_valid(x, y, N):
    return 1 <= x <= N and 1 <= y <= N


def moves(n, x1, y1, x2, y2):
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    queue = deque([(x1, y1)])
    visited = {(x1, y1): None}

    while queue:
        x, y = queue.popleft()
        if (x, y) == (x2, y2):
            break
        for i in range(8):
            new_x, new_y = x + dx[i], y + dy[i]
            if is_valid(new_x, new_y, n) and (new_x, new_y) not in visited:
                visited[(new_x, new_y)] = (x, y)
                queue.append((new_x, new_y))

    path = []
    current = (x2, y2)
    while current is not None:
        path.append(current)
        current = visited[current]
    path.reverse()
    return path


n = int(input())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

path = moves(n, x1, y1, x2, y2)
print(len(path) - 1)
for x, y in path:
    print(x, y)