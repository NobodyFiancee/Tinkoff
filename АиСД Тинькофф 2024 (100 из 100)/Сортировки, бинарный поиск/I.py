n = int(input())
pos = list(map(int, input().split()))

pos_set = set()
current_ans = n
res = [1]

for i in range(n):
    pos_set.add(pos[i])
    while current_ans in pos_set:
        pos_set.remove(current_ans)
        current_ans -= 1
    res.append(len(pos_set) + 1)

print(*res)