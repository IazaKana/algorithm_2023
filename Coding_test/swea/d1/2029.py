n = int(input())
A = [0] * n
B = [0] * n

for i in range(n):
    a, b = map(int, input().split())
    A[i] = a
    B[i] = b

for i in range(n):
    print('#' + str(i+1), A[i] // B[i], A[i] % B[i])