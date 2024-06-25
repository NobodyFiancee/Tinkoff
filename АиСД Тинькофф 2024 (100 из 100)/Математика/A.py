def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def min_rotations_to_return_to_initial_state(N, K):
    return lcm(N, K)

N, K = map(int, input().split())
print(min_rotations_to_return_to_initial_state(N, K))