p = input().strip()
t = input().strip()

ans = []
p_len = len(p)
t_len = len(t)
for i in range(t_len - p_len + 1):
    mismatch_count = 0
    for j in range(p_len):
        if t[i + j] != p[j]:
            mismatch_count += 1
            if mismatch_count > 1:
                break
    if mismatch_count <= 1:
        ans.append(i + 1)

print(len(ans))
print(*ans)