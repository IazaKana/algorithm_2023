A = [0] * 13

for i in range(1, 8):
    if i % 2 == 1:
        A[i] = 31
    elif i % 2 == 0:
        A[i] = 30
        if i == 2:
            A[i] = 28

for i in range(8, 13):
    if i % 2 == 1:
        A[i] = 30
    elif i % 2 == 0:
        A[i] = 31

n = int(input())
B = [0] * n

for i in range(n):
    B[i] = list(map(int, input()))

for i in range(n):
    a = 1000*B[i][0] + 100*B[i][1] + 10*B[i][2] + B[i][3]
    b= B[i][4] + B[i][5]
    c = 10 * B[i][6] + B[i][7]
    result = True

    if b < 1 or b > 13:
        result = False

    if c < 1 or c > A[b]:
        result = False

    print('#' + str(i+1), str(a) + '/' + str(b) + '/' + str(c)) if result == True else print('#' + str(i+1), '-1')
    