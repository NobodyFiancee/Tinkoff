sequence = input().strip()
length = len(sequence)
packed_sequence = [[''] * length for _ in range(length)]

for sub_length in range(1, length + 1):
    for start_index in range(length - sub_length + 1):
        end_index = start_index + sub_length - 1
        minimum = sequence[start_index:end_index + 1]

        if sub_length > 4:
            for right_index in range(start_index, end_index):
                left_index = right_index + 1
                temp = packed_sequence[start_index][right_index] + packed_sequence[left_index][end_index]
                if len(temp) < len(minimum):
                    minimum = temp

            for period_length in range(1, sub_length):
                if sub_length % period_length == 0:
                    is_periodic = all(sequence[i] == sequence[i - period_length] for i in range(start_index + period_length, end_index + 1))
                    if is_periodic:
                        temp = str(sub_length // period_length) + '(' + packed_sequence[start_index][start_index + period_length - 1] + ')'
                        if len(temp) < len(minimum):
                            minimum = temp

        packed_sequence[start_index][end_index] = minimum

print(packed_sequence[0][length - 1])
