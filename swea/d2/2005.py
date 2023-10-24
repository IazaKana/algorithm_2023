n = int(input())

for i in range(n):
    m = int(input())
    print('#' + str(i+1))
    for j in range(1, m+1):
        if j == 1:
            print('1')
        elif j == 2:
            a = 1
            print(a, a)
            A = [1, 1]
        else:
            B = [0] * j
            B[0] = 1
            B[j-1] = 1
            for k in range(1, j-1):
                B[k] = A[k-1] + A[k]
            print(*B)
            A = B

# print(*B) = 리스트 한칸씩 띄워서 한 줄 출력