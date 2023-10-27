n = int(input())

count = [0] * n
for i in range(n):
    a = map([int, input().split])
    count[i] = sum(a)
A = sorted(count)
for i in range(n):
    if A[0] <= count[i] and count[i] > A[n/10]:
        print('#' + str(i+1), 'D0')
    elif A[n/10] <= count[i] and count[i] > A[(n*2)/10]:
        print('#' + str(i+1), 'C-')
    elif A[(n*2)/10] <= count[i] and count[i] > A[(n*3)/10]:
        print('#' + str(i+1), 'C0')
    elif A[(n*3)/10] <= count[i] and count[i] > A[(n*4)/10]:
        print('#' + str(i+1), 'C+')
    elif A[(n*4)/10] <= count[i] and count[i] > A[(n*5)/10]:
        print('#' + str(i+1), 'B-')
    elif A[(n*5)/10] <= count[i] and count[i] > A[(n*6)/10]:
        print('#' + str(i+1), 'B0')
    elif A[(n*6)/10] <= count[i] and count[i] > A[(n*7)/10]:
        print('#' + str(i+1), 'B+')
    elif A[(n*7)/10] <= count[i] and count[i] > A[(n*8)/10]:
        print('#' + str(i+1), 'A-')
    elif A[(n*8)/10] <= count[i] and count[i] > A[(n*9)/10]:
        print('#' + str(i+1), 'A0')
    elif A[(n*9)/10] <= count[i] and count[i] > A[(n*10)/10]:
        print('#' + str(i+1), 'A+')