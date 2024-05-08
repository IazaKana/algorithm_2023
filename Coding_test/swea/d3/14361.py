N = int(input())

for i in range(N):
    num = input()
    num_list = sorted(list(num))

    answer = False

    k = 2
    while True:
        multi_num = int(num) * k
        if len(str(multi_num)) > len(num):
            break

        if sorted(list(str(multi_num))) == num_list:
            answer = True
            break
        k += 1

    if answer:
        result = 'possible'
    else:
        result = 'impossible'
    print('{}{} {}'.format('#', i+1, result))