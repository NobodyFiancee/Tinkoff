import bisect
import sys


class Center:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id


def read_centers():
    n = int(sys.stdin.readline().split()[2])
    centers = []
    for id in range(n):
        x, y = map(float, sys.stdin.readline().split())
        centers.append(Center(int(x * 2), int(y * 2), id))
    return centers


def calculate_x_indices(centers):
    y_values = sorted(set(center.y for center in centers))
    centers.sort(key=lambda center: center.x)
    return y_values


def get_x_sum(x_indices, index):
    x_sum = 0
    while index >= 0:
        x_sum += x_indices[index]
        index = (index & (index + 1)) - 1
    return x_sum


def update_x_indices(x_indices, index, extra):
    while index < len(x_indices):
        x_indices[index] += extra
        index |= index + 1


def calculate_distances(centers, y_values):
    x_indices = [0] * len(y_values)
    distances = [0] * len(centers)

    for center in centers:
        y_index = bisect.bisect_left(y_values, center.y)
        assert y_index != len(y_values) and y_values[y_index] == center.y

        dist = center.x - get_x_sum(x_indices, y_index)
        assert dist > 0 and distances[center.id] == 0

        distances[center.id] = dist

        y_index1 = bisect.bisect_right(y_values, center.y - dist)
        y_index2 = bisect.bisect_right(y_values, center.y + dist)
        update_x_indices(x_indices, y_index1, dist * 2)
        update_x_indices(x_indices, y_index2, -dist * 2)

    return distances


centers = read_centers()
y_values = calculate_x_indices(centers)
distances = calculate_distances(centers, y_values)

assert all(dist != 0 for dist in distances)

print(*distances)