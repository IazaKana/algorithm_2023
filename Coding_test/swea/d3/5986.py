prime = []
for i in range(2, 1000) :
    for j in range(2, i // 2 + 1) :
        if i % j == 0 :
            break
    else :
        prime.append(i)

t = int(input())
for tc in range(1, t + 1) :
    n = int(input())
    result = 0

    for i in range(len(prime)) :
        if prime[i] < n :
            for j in range(i, len(prime)) :
                if prime[j] < n :
                    for k in range(j, len(prime)) :
                        if prime[i] + prime[j] + prime[k] == n :
                            result += 1

    print('#%d %d' % (tc, result))