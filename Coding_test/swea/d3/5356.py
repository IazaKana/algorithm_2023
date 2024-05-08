T = int(input())

for i in range(1, T+1):
    A = list(input())
    B = list(input())
    C = list(input())
    D = list(input())
    E = list(input())
    answer = []
    max_num = max(len(A), len(B), len(C), len(D), len(E))

    for j in range(max_num):
        if j < len(A):
            answer.append(A[j])
        if j < len(B):
            answer.append(B[j])
        if j < len(C):
            answer.append(C[j])
        if j < len(D):
            answer.append(D[j])
        if j < len(E):
            answer.append(E[j])

    print('{}{}'.format('#', i), ''.join(answer))