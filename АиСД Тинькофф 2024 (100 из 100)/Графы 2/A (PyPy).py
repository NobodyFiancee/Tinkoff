class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.min_elem = list(range(n))
        self.max_elem = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        if self.rank[x_root] < self.rank[y_root]:
            x_root, y_root = y_root, x_root

        self.parent[y_root] = x_root
        self.size[x_root] += self.size[y_root]
        self.min_elem[x_root] = min(self.min_elem[x_root], self.min_elem[y_root])
        self.max_elem[x_root] = max(self.max_elem[x_root], self.max_elem[y_root])

        if self.rank[x_root] == self.rank[y_root]:
            self.rank[x_root] += 1

    def get(self, x):
        x_root = self.find(x)
        return self.min_elem[x_root], self.max_elem[x_root], self.size[x_root]


def main():
    n, m = map(int, input().split())
    dsu = DisjointSetUnion(n)

    for _ in range(m):
        operation, *args = input().split()
        if operation == "union":
            x, y = map(int, args)
            dsu.union(x - 1, y - 1)
        elif operation == "get":
            x = int(args[0])
            min_elem, max_elem, size = dsu.get(x - 1)
            print(min_elem + 1, max_elem + 1, size)


if __name__ == "__main__":
    main()