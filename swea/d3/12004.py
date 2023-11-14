N = int(input())

A = []
for x in range(1, 10):
    for y in range(1, 10):
        A.append(x * y)

for i in range(1, N+1):
    answer = 'No'
    num = int(input())
    if num in A:
        answer = 'Yes'
    print('{}{} {}'.format('#', i, answer))

#판단 문제로 풀어보기