n = int(input())
st = input()
counter = [0] * 26

for l in st:
    counter[ord(l) - ord('A')] += 1

half_result = ''
index_max = -1
max = -1
for i in range(26):
    if counter[i] != 0 and counter[i] % 2 == 1 and max < counter[i]:
        max = counter[i]
        index_max = i

for i in range(26):
    if counter[i] != 0 and counter[i] % 2 == 1:
        half_result += chr(i + ord('A')) * ((counter[i] - 1) // 2)
    elif counter[i] != 0 and counter[i] % 2 == 0:
        half_result += chr(i + ord('A')) * (counter[i] // 2)


if index_max != -1:
    print(''.join(half_result) + (chr(index_max + ord('A'))) + ''.join(half_result[::-1]))
else:
    print(''.join(half_result) + ''.join(half_result[::-1]))