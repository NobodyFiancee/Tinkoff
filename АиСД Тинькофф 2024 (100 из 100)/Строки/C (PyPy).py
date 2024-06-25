def get_hash(start, delta, hashes):
    return (hashes[start + delta] - hashes[start] * pw) % m


def create_hashes(s):
    hashes = [0] * (len(s) + 1)
    for i in range(1, len(hashes)):
        hashes[i] = (hashes[i - 1] * p + ord(s[i - 1])) % m
    return hashes


def count_cyclic_shifts(a, b):
    hashes_a = create_hashes(a)
    hashes_b = create_hashes(b * 2)

    hashes = set()
    for i in range(len_b + 1):
        hashes.add(get_hash(i, len_b, hashes_b))

    count = 0
    for i in range(len_a - len_b + 1):
        if get_hash(i, len_b, hashes_a) in hashes:
            count += 1
    return count


a = input()
b = input()

p = 31
m = 10 ** 9 + 9
len_a = len(a)
len_b = len(b)
pw = (p ** len_b) % m

print(count_cyclic_shifts(a, b))