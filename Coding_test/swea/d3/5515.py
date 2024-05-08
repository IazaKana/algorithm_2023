T = int(input())
A = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(1, T+1):
    m, d = map(int, input().split())
    sum = 0
    for j in range(1, m):
        sum += A[j]
    sum += d
    if sum % 7 == 1:
        answer = 4
    elif sum % 7 == 2:
        answer = 5
    elif sum % 7 == 3:
        answer = 6
    elif sum % 7 == 4:
        answer = 0
    elif sum % 7 == 5:
        answer = 1
    elif sum % 7 == 6:
        answer = 2
    elif sum % 7 == 0:
        answer = 3

    print('{}{} {}'.format('#', i, answer))