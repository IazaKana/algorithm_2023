n = input()

a = list(map(int, n))
a.sort(reverse = True)

for i in a:
    print(i, end='')