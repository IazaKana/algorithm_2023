T = int(input())

for i in range(1, T+1):
    A, B = map(int, input().split())
    answer = (A // B) ** 2
    print('{}{} {}'.format('#', i, answer))