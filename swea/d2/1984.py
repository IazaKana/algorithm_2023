n = int(input())

for i in range(n):
    A = list(map(int, input().split()))
    A.remove(max(A))
    A.remove(min(A))
    sum = 0
    for j in A:
        sum += j
    sum = round(sum // len(A))
    print('#' + str(i+1), sum)

#===================================

n = int(input()) 
for i in range(n):
    A = list(map(int, input().split()))
    A.sort()
    A.remove(A[0])
    A.remove(A[-1])

    M = round(sum(A) / len(A))