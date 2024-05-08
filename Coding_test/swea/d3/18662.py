n = int(input())

for i in range(n):
    a, b, c = map(int, input().split())
    m = (a + c) / 2
    answer = m - b
    print('{}{} {}'.format('#', i+1, abs(answer)))