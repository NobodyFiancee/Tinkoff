s = input()
min_shift = s
s += s
for i in range(len(min_shift)):
    if s[i:i + len(min_shift)] < min_shift:
        min_shift = s[i:i + len(min_shift)]
print(min_shift)