import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
p_list = list(map(int, input().split()))
si = 0
ei = 1
count = 0
p_list.sort()

while si < ei:
    if p_list[ei] + p_list[si] == m:
        count += 1
        si += 1
        ei = si + 1
    elif p_list[ei] + p_list[si] > m:
        si += 1
        ei = si + 1
    else:
        ei += 1

print(count)