n = int(input())

for i in range(n):
    A = list(map(int, input().split()))
    t1 = A[0] + A[2]
    t2 = A[1] + A[3]
    if t2 >= 60:
        t2 -= 60
        t1 += 1
    if t1 > 12:
        t1 -= 12
    print('#' + str(i+1), t1, t2)