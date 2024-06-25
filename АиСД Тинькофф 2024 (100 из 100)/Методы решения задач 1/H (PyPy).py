import heapq

def solve_tasks(n, c, tasks):
    total_score = 0
    solved_tasks = []

    current_time = 0
    pq = []

    for task_index, task in enumerate(tasks):
        start_time, duration = task
        heapq.heappush(pq, (start_time + duration, task_index))

    while pq:
        end_time, task_index = heapq.heappop(pq)
        start_time, duration = tasks[task_index]
        if start_time >= current_time:
            current_time = start_time + duration
            total_score += c
            solved_tasks.append(str(task_index + 1))

    return total_score, len(solved_tasks), solved_tasks


n, c = map(int, input().split())
tasks = [list(map(int, input().split())) for _ in range(n)]

max_score, num_solved, solved_tasks = solve_tasks(n, c, tasks)

print(max_score)
print(num_solved)
print(' '.join(solved_tasks))