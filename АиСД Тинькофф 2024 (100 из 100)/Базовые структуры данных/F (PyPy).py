import sys
from collections import deque

dek = deque()
c = {}

n = int(sys.stdin.readline())

for i in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == '1':
        dek.append(cmd[1])
        c[cmd[1]] = len(dek) - 1
    elif cmd[0] == '2':
        if dek:
            del c[dek.popleft()]
            for key in c:
                c[key] -= 1
    elif cmd[0] == '3':
        if dek:
            del c[dek.pop()]
    elif cmd[0] == '4':
        print(c.get(cmd[1], -1))
    elif cmd[0] == '5':
        print(dek[0])