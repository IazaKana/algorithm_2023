N = int(input())
M = int(input())
A = list(map(int, input().split()))
A.sort()
start = 0
end = N-1
count = 0
while start < end:
    if A[start] + A[end] == M:
        start += 1
        end -= 1
        count += 1
    elif A[start] + A[end] > M:
        end -= 1
    else:
        start += 1

print(count)