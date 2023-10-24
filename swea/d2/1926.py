n = int(input())

for i in range(1, n+1):
    a = str(i)
    count = 0
    for j in range(len(a)):
        if a[j] == '3' or a[j] == '6' or a[j] == '9':
            count += 1
    if count == 0:
        print(a, end=' ')
    elif count != 0:
        print('-'*count, end=' ')    

