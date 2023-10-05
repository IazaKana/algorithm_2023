import sys
input = sys.stdin.readline()
a, b = int(input().split())
p_list = []
sum = 0

for i in range(a):
    p_list.append(list(input().split()))

for i in range(a):
    for j in range(a):
        sum += p_list[i][j]

for i in range(b):
    