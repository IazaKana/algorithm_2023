n = int(input())
m1 = 50000
m2 = 10000
m3 = 5000
m4 = 1000
m5 = 500
m6 = 100
m7 = 50
m8 = 10

for i in range(n):
    N = int(input())
    A = [0] * 8
    a = 0
    if N >= m1:
        while N >= m1:
            N -= m1
            a += 1
        A[0] = a
        a = 0

    if N >= m2:
        while N >= m2:
            N -= m2
            a += 1
        A[1] = a
        a = 0

    if N >= m3:
        while N >= m3:
            N -= m3
            a += 1
        A[2] = a
        a = 0

    if N >= m4:
        while N >= m4:
            N -= m4
            a += 1
        A[3] = a
        a = 0

    if N >= m5:
        while N >= m5:
            N -= m5
            a += 1
        A[4] = a
        a = 0

    if N >= m6:
        while N >= m6:
            N -= m6
            a += 1
        A[5] = a
        a = 0

    if N >= m7:
        while N >= m7:
            N -= m7
            a += 1
        A[6] = a
        a = 0

    if N >= m8:
        while N >= m8:
            N -= m8
            a += 1
        A[7] = a
        a = 0

    print('#'+ str(i+1))
    print(*A)

#다음번에는 간결하게 바꾸기