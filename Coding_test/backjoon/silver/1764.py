import sys

N, M = map(int, input().split())
set_a = set()
set_b = set()

for i in range(N):
    a = sys.stdin.readline()
    set_a.add(a)

for i in range(M):
    b = sys.stdin.readline()
    set_b.add(b)

result = sorted(set_a & set_b)

print(len(result))

for i in result:
    print(i)
    
