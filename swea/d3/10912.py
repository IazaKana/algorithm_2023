N = int(input())

for i in range(N):
    a = list(input())
    C = list()
    for j in a:
        if j in C:
            C.remove(j)
        elif j not in C:
            C.append(j)
    if len(C) == 0:
        answer = 'Good'
    else:
        C.sort()
        answer = ''.join(C)
    print('{}{} {}'.format('#', i+1, answer))

