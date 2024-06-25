from collections import defaultdict, deque


def min_distance_bfs(graph, start, end):
    queue = deque()
    queue.append((start, 0))
    visited = {}

    while queue:
        value, depth = queue.popleft()
        if value not in visited:
            for i in graph[value]:
                queue.append((i, depth + 1))
            visited[value] = depth
        elif visited[value] > depth + 1:
            visited[value] = depth + 1
        if value == end:
            return visited[value]

    return -1


m = int(input())

graph = defaultdict(list)
for i in range(m):
    x, y = input().split(' -> ')
    graph[x].append(y)

start = input()
end = input()

print(min_distance_bfs(graph, start, end))