n = int(input())

for i in range(n):
    N = int(input())
    A = []
    m = 0
    while len(A) < 10:
        m += 1
        N1 = N * m
        Ns = [int(x) for x in str(N1)]
        for j in Ns:
            if j not in A:
                A.append(j)
    print('{}{} {}'.format('#', i+1, N*m))

#while문 조건 -> 잘못하면 무한루프 조심