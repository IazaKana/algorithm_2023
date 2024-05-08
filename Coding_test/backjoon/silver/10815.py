def solution(A, num):
    left = 0
    right = len(A) - 1
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        if num == A[mid]:
            answer = 1
            break
        elif num > A[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return answer

N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
test = list(map(int, input().split()))

for i in test:
    print(solution(A, i), end=' ')
    