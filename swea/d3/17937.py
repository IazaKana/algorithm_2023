n = int(input())

for i in range(n):
    A, B = map(int, input().split())
    answer = 0
    if A == B:
        answer = A
    else:
        answer = 1
    print('{}{} {}'.format('#', i+1, answer))