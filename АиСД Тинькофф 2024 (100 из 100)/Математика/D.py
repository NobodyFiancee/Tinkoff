def last_non_zero_digit_factorial(N):
    product = 1
    count_twos = 0
    count_fives = 0

    for i in range(1, N + 1):
        current = i
        while current % 2 == 0:
            count_twos += 1
            current //= 2
        while current % 5 == 0:
            count_fives += 1
            current //= 5
        product *= current
        product %= 10

    excess_twos = count_twos - count_fives
    for _ in range(excess_twos):
        product *= 2
        product %= 10

    return product


N = int(input())
result = last_non_zero_digit_factorial(N)
print(result)
