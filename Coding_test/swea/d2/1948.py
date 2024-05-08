n = int(input())
A = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(n):
    m1, n1, m2, n2 = map(int, input().split())
    answer = 0
    if m2 - m1 >= 2:
        for j in range(m1+1, m2):
            answer += A[j]
        answer += n2
        answer += (A[m1] - n1)
    elif m2 == m1:
        answer = n2 - n1
    print('{}{} {}'.format('#', i+1, answer + 1))