def z_function(st):
    prefix_function = [0] * len(st)
    border = 0
    for i in range(1, len(st)):
        while border > 0 and st[i] != st[border]:
            border = prefix_function[border - 1]
        if st[i] == st[border]:
            border += 1
        else:
            border = 0
        prefix_function[i] = border
    return prefix_function


def kmp(text, st):
    prefix_function = z_function(st)
    index_result = []
    border = 0
    for i in range(len(text)):
        while border > 0 and text[i] != st[border]:
            border = prefix_function[border - 1]
        if text[i] == st[border]:
            border += 1
        else:
            border = 0
        if border == len(st):
            index_result.append(i - len(st) + 1)
            border = prefix_function[border - 1]
    return index_result


t = input()
q = int(input())

for _ in range(q):
    s = input()
    result = kmp(t, s)
    print(len(result), *result)