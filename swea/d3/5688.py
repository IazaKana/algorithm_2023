T = int(input())

for i in range(1, T + 1):
    N = int(input())
    answer = -1
    for j in range(1, N + 1):
        if j * j * j > N:
            break

        if j * j * j == N:
            answer = j
            break

    print('{}{} {}'.format('#', i, answer))