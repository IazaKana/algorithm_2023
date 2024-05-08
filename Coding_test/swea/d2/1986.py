n = int(input())

for i in range(n):
    a = int(input())
    sum = 0
    for j in range(1, a+1):
        if j % 2 == 0:
            sum -= j
        else:
            sum += j
    print('#' + str(j), sum)