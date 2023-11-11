# import sys
# input = sys.stdin.readline
# from collections import deque
# N, K = map(int, input().split())
# A = deque()
# sum = 0
# count  = 0

# for i in range(N):
#     A.appendleft(int(input()))

# for i in A:
#     while sum + i <= K:
#         sum += i
#         count += 1
#     if sum == K:
#         print(count)
#         break

#=================================

N, K = map(int, input().split())
A = [0] * N

for i in range(N):
    A[i] = int(input())

count = 0

for i in range(N-1, -1, -1):
    if A[i] <= K:
        count += int(K / A[i])
        K = K % A[i]

print(count)