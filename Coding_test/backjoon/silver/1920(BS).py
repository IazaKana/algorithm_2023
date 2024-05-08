def solution(A, num):
    left = 0
    right = N - 1
    answer = False

    while left <= right:
        mid = (left + right) // 2
        if num == A[mid]:
            answer = True
            print(1)
            break
        elif num > A[mid]:
            left = mid + 1
        else:
            right = mid - 1
    if not answer:
        print(0)


N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
B = list(map(int, input().split()))

for i in B:
    solution(A, i)