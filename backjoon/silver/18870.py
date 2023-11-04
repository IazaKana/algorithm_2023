# import sys
# n = int(input())
# A = list()

# for i in range(n):
#     A.append(int(sys.stdin.readline()))

# A.sort()

# for i in A:
#     print(i)

N = int(input())

A = list(map(int, input().split()))
B = list(set(A))
B.sort()

test = {B[i] : i for i in range(len(B))}
for k in A:
    print(test[k], end=' ')
#딕셔너리 선언