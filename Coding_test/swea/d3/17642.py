n = int(input())

for i in range(n):
    A, B = map(int, input().split())
    A, B = min(A, B), max(A, B)
    answer = 0
    if A == B:
        answer = 0
    elif B-A == 1:
        answer = -1
    elif (B-A) % 2 == 0:
        answer = (B-A) // 2
    elif (B-A) % 2 == 1:
        answer = (B-A) // 2
    print('{}{} {}'.format('#', i+1, answer))

#미해결