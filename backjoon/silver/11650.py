import sys
N = int(input())
A = []

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    A.append([a, b])

A.sort(key = lambda v : (v[0], v[1]))
for x, y in A:
    print(x, y)