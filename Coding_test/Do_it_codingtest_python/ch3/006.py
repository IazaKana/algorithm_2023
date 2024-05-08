n = int(input())
count = 1
si = 1
ei = 1
sum = 1

while ei != n:
    if sum == n:
        count += 1
        si += 1
        ei = si
        sum = si
    elif sum > n:
        si += 1
        ei = si
        sum = si
    else:
        ei += 1
        sum += ei

print(count)