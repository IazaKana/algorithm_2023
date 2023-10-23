a = int(input())

for v in range(a):
    b = int(input())
    A = list(map(int, input().split()))
    mn = A[-1]
    sum = 0
    for i in range(b-1, -1, -1):
        if A[i] > mn:
            mn = A[i]
        else:
            sum += mn - A[i]
    print('#{} {}'.format(v+1, sum))