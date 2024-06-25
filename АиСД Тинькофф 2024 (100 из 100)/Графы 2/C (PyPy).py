rows, columns = map(int, input().split())

def encode(row, column):
    return row * (columns + 1) + column

parent = [-1] * (1 + encode(rows + 1, columns + 1))

def find_root(node):
    if parent[node] < 0:
        return node
    else:
        root = find_root(parent[node])
        parent[node] = root
        return root

def unite(a, b):
    a = find_root(a)
    b = find_root(b)
    if a == b:
        return False
    assert parent[a] < 0
    assert parent[b] < 0
    if parent[a] < parent[b]:
        parent[a] += parent[b]
        parent[b] = a
    else:
        parent[b] += parent[a]
        parent[a] = b
    return True

for row in range(1, rows + 1):
    line = list(map(int, input().split()))
    for column in range(1, columns + 1):
        code = line[column - 1]
        if code & 1:
            unite(encode(row, column), encode(row + 1, column))
        if code & 2:
            unite(encode(row, column), encode(row, column + 1))

result_rows, result_columns, result_directions = [], [], []
result_cost = 0

for row in range(1, rows):
    for column in range(1, columns + 1):
        if unite(encode(row, column), encode(row + 1, column)):
            result_rows.append(row)
            result_columns.append(column)
            result_directions.append(1)
            result_cost += 1

for row in range(1, rows + 1):
    for column in range(1, columns):
        if unite(encode(row, column), encode(row, column + 1)):
            result_rows.append(row)
            result_columns.append(column)
            result_directions.append(2)
            result_cost += 2

print(len(result_rows), result_cost)
for i in range(len(result_rows)):
    print(result_rows[i], result_columns[i], result_directions[i])