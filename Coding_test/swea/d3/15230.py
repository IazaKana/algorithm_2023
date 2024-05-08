A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
N = int(input())

for i in range(N):
    a = list(input())
    count = 0
    for j in range(len(a)):
        if a[j] == A[j]:
            count += 1
        else:
            break
    print('{}{} {}'.format('#', i+1, count))