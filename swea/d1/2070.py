n = int(input())
A = []

for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        A.append('>')
    elif a < b:
        A.append('<')
    elif a == b:
        A.append('=')

for i in range(n):
    print('#' + str(i + 1), A[i])