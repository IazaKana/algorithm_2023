n = 10
A = [[1, 3], [2, 5],[5, 8]]
for [x, y] in A:
    m = y-x
    n = min(m, n)
print(n)