import sys
input = sys.stdin.readline
n, m = map(int, input().split())
l = list(input())
a, b, c, d = input().split()
sH = {'A': a, 'C': b, 'G': c, 'T':d}
e = a + b + c + d

for i in range(len(m-n)):
    l[i]