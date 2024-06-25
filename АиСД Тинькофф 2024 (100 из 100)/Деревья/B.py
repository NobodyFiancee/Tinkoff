import sys
from collections import deque


class Node:
    def __init__(self, value, l_c=-1, r_c=-1):
        self.value: int = value
        self.left_children = l_c
        self.right_children = r_c


class Tree:
    def __init__(self, n):
        self.nodes = [Node(i) for i in range(n)]
        self.is_avl = True

    def add(self, i, l_c, r_c):
        self.nodes[i].left_children = l_c
        self.nodes[i].right_children = r_c

    def height(self, node_index):
        node = self.nodes[node_index]
        if node.left_children == -1 and node.right_children == -1:
            return 0

        left_height = right_height = 0
        if node.left_children != -1:
            left_height = 1 + self.height(node.left_children)
        if node.right_children != -1:
            right_height = 1 + self.height(node.right_children)

        return max(left_height, right_height)

    def dfs(self, root):
        stack = deque([root])

        while stack:
            node_index = stack.pop()
            node = self.nodes[node_index]

            if node.left_children != -1:
                left_child = self.nodes[node.left_children]
                if left_child.value >= node.value:
                    self.is_avl = False
                    break

                stack.append(node.left_children)

            if node.right_children != -1:
                right_child = self.nodes[node.right_children]
                if right_child.value <= node.value:
                    self.is_avl = False
                    break

                stack.append(node.right_children)

            left_height = 0 if node.left_children == -1 else 1 + self.height(node.left_children)
            right_height = 0 if node.right_children == -1 else 1 + self.height(node.right_children)

            if abs(left_height - right_height) > 1:
                self.is_avl = False
                break

    def is_avl_tree(self, root):
        self.dfs(root)
        return 1 if self.is_avl else 0


sys.setrecursionlimit(10 ** 8)
n, r = map(int, sys.stdin.readline().split())
tree = Tree(n)
for i in range(n):
    l_c, r_c = map(int, sys.stdin.readline().split())
    tree.add(i, l_c, r_c)

print(tree.is_avl_tree(r))