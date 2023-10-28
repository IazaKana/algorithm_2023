n = int(input())

for i in range(n):
    m = int(input())
    a = b = c = d = e = 0
    while m % 2 == 0:
        a +=1
        m //= 2
    while m % 3 == 0:
        b += 1
        m //= 3
    while m % 5 == 0:
        c += 1
        m //= 5
    while m % 7 == 0:
        d += 1
        m //= 7
    while m % 11 == 0:
        e += 1
        m //= 11
    # if m == 1:
    print('{}{} {} {} {} {} {}'.format('#', i+1, a, b, c, d, e))