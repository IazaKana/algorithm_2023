n = int(input())

for i in range(n):
    a = str(input())
    if len(a) % 2 == 0: #짝수일때
        if a[0:len(a)//2] == a[len(a)-1:len(a)//2-1:-1]:
            print('#' + str(i+1), '1')
        else:
            print('#' + str(i+1), '0')
    elif len(a) % 2 == 1: #홀수일때
        if a[0:len(a)//2] == a[len(a)-1:len(a)//2:-1]:
            print('#' + str(i+1), '1')
        else:
            print('#' + str(i+1), '0')

#인덱스 역정렬