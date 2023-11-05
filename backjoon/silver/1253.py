N = int(input())
A = list(map(int, input().split()))
A.sort()
count = 0

for i in range(N):
    start = 0
    end = N-1
    find = A[i]
    while start < end:
        if A[start] + A[end] == find:
            if start != i and end != i:
                count += 1
                break
            elif start == i:
                start += 1
            elif end == i:
                end -= 1

        elif A[start] + A[end] > find:
            end -= 1
        else:
            start += 1

print(count)