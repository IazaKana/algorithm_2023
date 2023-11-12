N = int(input())
for i in range(N):
    a = int(input())
    if a % 2 == 0:
        print('{}{} {}'.format('#', i+1, 'Alice'))
    else:
        print('{}{} {}'.format('#', i+1, 'Bob'))