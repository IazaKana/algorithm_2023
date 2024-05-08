n = int(input())

def solution(a, b):
    answer = 0
    for j in range(len(a)-len(b)+1):
        sum = 0
        for k in range(len(b)):
            sum += a[k+j] * b[k]
        answer = max(answer, sum)
    return print('#' + str(i+1), answer)


for i in range(n):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if len(A) >= len(B):
        solution(A, B)
    else:
        solution(B, A)