n = int(input())

for i in range(1, n+1):
    m = int(input())
    count = 0
    for nx in range(-m, m+1):
        for ny in range(-m, m+1):
            if nx**2 + ny**2 <= m**2:
                count += 1
    print('{}{} {}'.format('#', i, count))