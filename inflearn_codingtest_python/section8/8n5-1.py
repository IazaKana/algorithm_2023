from collections import deque
def solution(nums):
    answer = 0
    A = deque(nums)
    i = 0
    while len(A) > 0:
        A.popleft()
        if len(A) == 1:
            return A[0]
        A.popleft()
        if len(A) == 1:
            return A[0]
        A.append(A.popleft())
        if len(A) == 1:
            return A[0]
        
print(solution([3, 1, 4, 5, 2, 6, 7]))
print(solution([10, 8, 3, 1, 4, 5, 2, 6, 7, 9]))
print(solution([10, 8, 3, 11, 12, 1, 4, 5, 2, 6, 7, 9]))
print(solution([10, 8, 3, 1, 4, 5, 2, 11, 13, 6, 7, 12, 9, 14]))
print(solution([1, 8, 6, 10, 4, 7, 2, 5, 3, 9]))