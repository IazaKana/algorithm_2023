n = int(input())

for i in range(n):
    m = int(input())
    A = []
    for j in range(m):
        a, b = input().split()
        for k in range(int(b)):
            A.append(a)
    
    print('{}{}'.format('#', i+1))
    for j in range(0, len(A)):
        if j == 0:
            print(A[j], end='')
        elif j % 10 == 9:
            print(A[j])
        elif j == len(A)-1:
            print(A[j])
        else:
            print(A[j], end='')
