def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    return is_prime


def find_goldbach_pair(n):
    is_prime = sieve_of_eratosthenes(n)

    for p in range(2, n):
        if is_prime[p]:
            q = n - p
            if q >= p and is_prime[q]:
                return p, q


n = int(input())
p, q = find_goldbach_pair(n)
print(p, q)
