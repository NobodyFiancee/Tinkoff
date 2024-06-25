from functools import lru_cache


@lru_cache
def count_safe_stacks(remaining_containers, previous_container_type):
    if remaining_containers == 0:
        return 1

    count = 0
    for container_type in ['A', 'B', 'C']:
        if container_type == 'A' and previous_container_type == 'A':
            continue
        count += count_safe_stacks(remaining_containers - 1, container_type)

    return count


n = int(input())
print(count_safe_stacks(n, ''))