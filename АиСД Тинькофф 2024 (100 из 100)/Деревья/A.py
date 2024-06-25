import sys
from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


class Tree:
    def __init__(self, n, parents):
        self.nodes = [Node(i) for i in range(n)]
        for i in range(1, n):
            parent = parents[i - 1]
            self.nodes[parent].children.append(self.nodes[i])
            self.nodes[i].children.append(self.nodes[parent])

    def bfs(self, start):
        visited = {start}
        queue = deque([(start, 0)])
        max_distance = 0
        farthest_node = start

        while queue:
            node, distance = queue.popleft()
            if distance > max_distance:
                farthest_node = node
                max_distance = distance

            for child in self.nodes[node].children:
                if child.value not in visited:
                    visited.add(child.value)
                    queue.append((child.value, distance + 1))

        return farthest_node, max_distance

    def diameter(self, start_node):
        #start_node, max_depth = self.bfs(0)
        _, diameter = self.bfs(start_node)
        return diameter



from collections import defaultdict
sys.setrecursionlimit(10**7)

def dfs(node, parent, depth, depths, max_depth, farthest_node):
    if depth > max_depth[0]:
        max_depth[0] = depth
        farthest_node[0] = node
    depths[node] = depth
    for child in tree[node]:
        if child != parent:
            dfs(child, node, depth + 1, depths, max_depth, farthest_node)

n = int(input())
tree = defaultdict(list)
parents = list(map(int, input().split()))

for i in range(1, n):
    tree[i].append(parents[i-1])
    tree[parents[i-1]].append(i)

farthest_node = [0]
max_depth = [0]
depths = [0] * n
dfs(0, -1, 0, depths, max_depth, farthest_node)

max_depth2 = max_depth[0]
depths_res = depths.copy()

farthest = farthest_node[0]
max_depth = [0]
dfs(farthest, -1, 0, depths, max_depth, farthest_node)

result = []
for node in range(n):
    result.append(str(depths_res[node]))

print(max_depth2, max_depth[0])
print(' '.join(result))