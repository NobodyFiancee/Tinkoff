def largest_rectangle_area(heights):
    max_area = 0
    stack = []

    for i, height in enumerate(heights):
        start_index = i
        while stack and stack[-1][1] >= height:
            index, h = stack.pop()
            start_index = index
            max_area = max(max_area, (i - index) * h)
        stack.append((start_index, height))

    for i, h in stack:
        max_area = max(max_area, (len(heights) - i) * h)

    return max_area


n = int(input())
heights = list(map(int, input().split()))
print(largest_rectangle_area(heights))
