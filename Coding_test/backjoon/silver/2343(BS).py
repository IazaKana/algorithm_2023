N, M = int(input().split())
A = list(map(int, input().split()))
start = end = 0

for i in A:
    if start < i:
        start = i
    end += i

while start <= end:
    mid = int((start + end) // 2)
    sum = 0
    count = 0
    