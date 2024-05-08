n = int(input())

for i in range(n):
    a = str(input())
    A = [a[0]]
    for j in range(1, len(a)):
        if a[j] == a[0] and j*2 <= len(a):
            b = " ".join(A)
            B = []
            for k in range(j, j*2):
                B.append(a[k])
            c = " ".join(B)
            if b == c:
                print('#' + str(i+1), j)
                break
        A.append(a[j])


