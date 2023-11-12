import sys
input = sys.stdin.readline
N = int(input())

def solution(A, B):
    while True:
        C = A % B
        if C == 0:
            return B
        A = B
        B = C

for i in range(N):
    A, B = map(int, input().split())
    num1 = max(A, B)
    num2 = min(A, B)
    num = solution(num1, num2)
    print(A*B // num)
