def get_adjacent_cells(x, y, rows, cols):
    adjacent_cells = []
    if x > 0:
        adjacent_cells.append((x - 1, y))
    if x < rows - 1:
        adjacent_cells.append((x + 1, y))
    if y > 0:
        adjacent_cells.append((x, y - 1))
    if y < cols - 1:
        adjacent_cells.append((x, y + 1))
    return adjacent_cells


def depth_first_search(x, y, grid, visited, rows, cols):
    stack = [(x, y)]
    ship_cells = []
    while stack:
        current_x, current_y = stack.pop()
        if visited[current_x][current_y]:
            continue
        visited[current_x][current_y] = True
        ship_cells.append((current_x, current_y))
        for neighbor_x, neighbor_y in get_adjacent_cells(current_x, current_y, rows, cols):
            if grid[neighbor_x][neighbor_y] in {'#', 'X'} and not visited[neighbor_x][neighbor_y]:
                stack.append((neighbor_x, neighbor_y))
    return ship_cells


def identify_ship_type(cells, grid):
    has_whole = any(grid[x][y] == '#' for x, y in cells)
    has_destroyed = any(grid[x][y] == 'X' for x, y in cells)
    if has_whole and not has_destroyed:
        return 'whole'
    elif has_destroyed and not has_whole:
        return 'destroyed'
    else:
        return 'damaged'


def count_ships(rows, cols, grid):
    visited = [[False] * cols for _ in range(rows)]
    whole_ships_count = 0
    damaged_ships_count = 0
    destroyed_ships_count = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] in {'#', 'X'} and not visited[i][j]:
                ship_cells = depth_first_search(i, j, grid, visited, rows, cols)
                ship_type = identify_ship_type(ship_cells, grid)
                if ship_type == 'whole':
                    whole_ships_count += 1
                elif ship_type == 'damaged':
                    damaged_ships_count += 1
                elif ship_type == 'destroyed':
                    destroyed_ships_count += 1

    return whole_ships_count, damaged_ships_count, destroyed_ships_count


rows, cols = map(int, input().split())
grid = []
for _ in range(rows):
    grid.append(list(input().strip()))
whole_ships_count, damaged_ships_count, destroyed_ships_count = count_ships(rows, cols, grid)
print(whole_ships_count, damaged_ships_count, destroyed_ships_count)


