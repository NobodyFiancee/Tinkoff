import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.depth = 0
        self.ancestors = [None] * 20


class Tree:
    def __init__(self, n, parents):
        self.nodes = [Node(i) for i in range(n)]
        for i in range(1, n):
            parent = parents[i - 1]
            self.nodes[i].parent = parent
            self.nodes[i].depth = self.nodes[parent].depth + 1
            self.nodes[i].ancestors[0] = parent
            for j in range(1, 20):
                if self.nodes[i].ancestors[j - 1] is not None:
                    self.nodes[i].ancestors[j] = self.nodes[self.nodes[i].ancestors[j - 1]].ancestors[j - 1]

    def lca(self, u, v):
        if self.nodes[u].depth > self.nodes[v].depth:
            u, v = v, u
        for i in range(19, -1, -1):
            if self.nodes[v].ancestors[i] is not None and self.nodes[self.nodes[v].ancestors[i]].depth >= self.nodes[u].depth:
                v = self.nodes[v].ancestors[i]
        if u == v:
            return u
        for i in range(19, -1, -1):
            if self.nodes[u].ancestors[i] != self.nodes[v].ancestors[i]:
                u = self.nodes[u].ancestors[i]
                v = self.nodes[v].ancestors[i]
        return self.nodes[u].parent


n = int(sys.stdin.readline())
parents = list(map(int, sys.stdin.readline().split()))

tree = Tree(n, parents)

m = int(sys.stdin.readline())

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    print(tree.lca(u, v))