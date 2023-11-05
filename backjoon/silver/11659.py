import sys
N, M = map(int, input().split())
A = list(map(int, input().split()))

def solution(A, num):
    sum = 0
    for i in range(num):
        sum += A[i]
    return sum

for i in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(solution(A,b)-solution(A,a)+A[a-1])

#==========================================================
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = [0]
temp = 0

for i in A:
    temp += i
    B.append(temp)

for i in range(M):
    a, b = map(int, input().split())
    print(B[b] - B[a-1])