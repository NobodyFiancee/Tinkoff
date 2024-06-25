def prime_factors(N):
    factors = []
    while N % 2 == 0:
        factors.append(2)
        N //= 2

    for i in range(3, int(N**0.5) + 1, 2):
        while N % i == 0:
            factors.append(i)
            N //= i

    if N > 2:
        factors.append(N)

    return factors


def format_factors(factors):
    if not factors:
        return ""

    factor_count = {}
    for factor in factors:
        if factor in factor_count:
            factor_count[factor] += 1
        else:
            factor_count[factor] = 1

    formatted_factors = []
    for factor in sorted(factor_count):
        if factor_count[factor] > 1:
            formatted_factors.append(f"{factor}^{factor_count[factor]}")
        else:
            formatted_factors.append(f"{factor}")

    return "*".join(formatted_factors)


N = int(input())
factors = prime_factors(N)
print(format_factors(factors))