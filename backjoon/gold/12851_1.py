n, m = map(int, input().split())

count = 0

def sub1(count, m):
    m -= 1
    count += 1
    return count, m

def add1(count, m):
    m += 1
    count += 1
    return count, m

def div1(count, m):
    m //= 2

def case1(count, m, n):
    while m > n*2:
        if m % 2 == 1:
            sub1(count, m)
        else:
            div1(count, m)
        count += 1

# 처음값이 홀수이고 값 > 목표값 * 2인경우
if m % 2 == 1 and m > n*2:
    pass
    #+1, -1 두가지 연산 케이스로 분류
    #+1 경우
    m1 = m
    count1 = count
    add1(count1, m1)
    # while m > n*2:
    #     if m % 2 == 1:
    #         sub1(count, m)
    #     else:
    #         div1(count, m)
    case1(count1, m1, n)
    #값 <= 목표값 * 2인 순간
    #값이 홀수 일떄
    if m1 % 2 == 1:
        #+1연산이후 나누기 2 연산 이후 +1 연산으로 가는 경우
        m1_1 = m1
        count1_1 = count1
        add1(count1_1, m1_1)
        div1(count1_1, m1_1)
        count1_1 += n - m1_1

        # -1연산이후 나누기 2 연산 이후 +1 연산으로 가는 경우
        m1_2 = m1
        count1_2 = count1
        sub1(count1_2, m1_2)
        div1(count1_2, m1_2)
        count1_2 += n - m1_2

        # -1연산으로만 가는 경우
        m1_5 = m1
        count1_5 = count1 + (m1_5 - n)

    #값이 짝수 일때
    else:
        #나누기 2 연산이후 +1연산으로 가는 경우
        m1_3 = m1
        count1_3 = count1
        div1(count1_3, m1_3)
        count1_3 += n - m1_3

        #-1연산으로만 가는 경우
        m1_4 = m1
        count1_4 = count1 + (m1_4 - n)

    #-1인 경우
    m2 = m
    count2 = count
    sub1(count, m)
    case1(count, m, n)
    #값이 홀수 일떄
    if m2 % 2 == 1:
        #+1연산이후 나누기 2 연산 이후 +1 연산으로 가는 경우
        m2_1 = m2
        count2_1 = count2
        add1(count2_1, m2_1)
        div1(count2_1, m2_1)
        count2_1 += n - m2_1

        # -1연산이후 나누기 2 연산 이후 +1 연산으로 가는 경우
        m2_2 = m2
        count2_2 = count2
        sub1(count2_2, m2_2)
        div1(count2_2, m2_2)
        count2_2 += n - m2_2

        # -1연산으로만 가는 경우
        m2_5 = m2
        count2_5 = count2 + (m2_5 - n)

    #값이 짝수 일때
    else:
        #나누기 2 연산이후 +1연산으로 가는 경우
        m2_3 = m2
        count2_3 = count2
        div1(count2_3, m2_3)
        count2_3 += n - m2_3

        #-1연산으로만 가는 경우
        m2_4 = m2
        count2_4 = count2 + (m2_4 - n)


# 처음값이 짝수이고 값 > 목표값 * 2인경우
elif m % 2 == 0 and m > n*2:
    
    #나누기 연산 진행

# 처음값이 홀수이고 값 <= 목표값 * 2인경우
elif m % 2 == 1 and m <= n*2:
    pass

# 처음값이 짝수이고 값 <= 목표값 * 2인경우
elif m % 2 == 0 and m <= n*2:
    pass