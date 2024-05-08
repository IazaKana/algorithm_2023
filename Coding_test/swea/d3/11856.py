N = int(input())

for i in range(N):
    A = []
    C = []
    B = list(input())
    for j in B:
        if j not in A:
            A.append(j)
            if j not in C:
                C.append(j)
        elif j in A:
            A.remove(j)
    if len(A) == 0 and len(C) == 2:
        answer = 'Yes'
    else:
        answer = 'No'

    print('{}{} {}'.format('#', i+1, answer))

#딕셔너리도 해보기