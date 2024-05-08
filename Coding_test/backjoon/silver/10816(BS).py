# N = int(input())
# A = list(map(int, input().split()))
# A.sort()
# M = int(input())
# arr = list(map(int, input().split()))

# def solution(A, num):
#     left = 0
#     right = N - 1
#     cnt = 0
#     while left <= right:
#         mid = (left + right) // 2
#         if num == A[mid]:
#             cnt += 1
#             left += 1
#             right += 1


# for i in arr:
#     solution(A, i)

from collections import Counter
N = int(input())
A = list(map(int, input().split()))
nA = Counter(A)
M = int(input())
arr = list(map(int, input().split()))

for i in arr:
    print(nA[i], end=' ')