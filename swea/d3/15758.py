n = int(input())

for i in range(1, n+1):
    a, b = input().split()
    a1 = len(a)
    b1 = len(b)
    answer = 0
    if  a * b1 == b * a1:
        answer = 'yes'
    else:
        answer = 'no'
    print('{}{} {}'.format('#', i, answer))