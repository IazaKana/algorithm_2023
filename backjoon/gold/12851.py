n, m = map(int, input().split())

count = 0

#값 > 목표값 * 2를 만족하는 동안 사용하는 +-연산
def as1(count, m):
    m -= 1

#값 > 목표값 * 2를 만족하는 동안 사용하는 /연산
def div1():
    m //= 2

def as2():
    pass

def div2():
    pass

if m % 2 == 1 and m > n*2:
    #-1연산한 경우
    m = m - 1
    count += 1
    count_1 = count
    m_1 = m
    while m_1 > n * 2:
        if m_1 % 2 == 0:
            m_1 //= 2
        else:
            m_1 -= 1
        count_1 += 1
    #값 < 목표값 * 2인 순간
    if m_1 % 2 == 1:
        # +1인경우
        count_1_1 = count_1
        m_1_1 = m_1
        m_1_1 += 1
        count_1_1 += 1
        # 나누기 2 연산 이후 +1 연산으로 가는 경우
        m_1_1_1 = m_1_1
        m_1_1_1 //= 2
        count_1_1_1 = count_1_1
        count_1_1_1 += 1 + (n-m_1_1_1)
        # -1연산으로만 가는 경우
        count_1_1_2 = count_1_1
        count_1_1_2 += (m_1_1-n)

        # -1인경우
        count_1_2 = count_1
        m_1_2 = m_1
        m_1_2 -= 1
        count_1_2 += 1
        # 나누기 2 연산 이후 +1 연산으로 가는 경우
        m_1_2_1 = m_1_2
        m_1_2_1 //= 2
        count_1_2_1 = count_1_2
        count_1_2_1 += 1 + (n-m_1_2_1)
        # -1연산으로만 가는 경우
        count_1_2_2 = count_1_2
        count_1_2_2 += (m_1_2-n)

    else:
        # 짝수인 경우
        count_1_3 = count_1
        m_1_3 = m_1
        # 나누기 2 연산 이후 +1 연산으로 가는 경우
        m_1_3_1 = m_1_3
        m_1_3_1 //= 2
        count_1_3_1 = count_1_3
        count_1_3_1 += 1 + (n-m_1_3_1)
        # -1연산으로만 가는 경우
        m_1_3_2 = m_1_3
        count_1_3_2 = count_1_3
        count_1_3_2 += (m_1_3-n)

    #+1연산한 경우
    count_2 = count
    m_2 = m
    while m_2 > n * 2:
        if m_2 % 2 == 0:
            m_2 //= 2
        else:
            m_2 -= 1
        count_2 += 1
    #값 < 목표값 * 2인 순간
    if m_2 % 2 == 1:
        # +1인경우
        count_2_1 = count_2
        m_2_1 = m_2
        m_2_1 += 1
        count_2_1 += 1
        # 나누기 2 연산 이후 +1 연산으로 가는 경우
        m_2_1_1 = m_2_1
        m_2_1_1 //= 2
        count_2_1_1 = count_2_1
        count_2_1_1 += 1 + (n-m_2_1_1)
        # -1연산으로만 가는 경우
        count_2_1_2 = count_2_1
        count_2_1_2 += (m_2_1-n)

        # -1인경우
        count_2_2 = count_2
        m_2_2 = m_2
        m_2_2 -= 1
        count_2_2 += 1
        # 나누기 2 연산 이후 +1 연산으로 가는 경우
        m_2_2_1 = m_2_2
        m_2_2_1 //= 2
        count_2_2_1 = count_2_2
        count_2_2_1 += 1 + (n-m_2_2_1)
        # -1연산으로만 가는 경우
        count_2_2_2 = count_2_2
        count_2_2_2 += (m_2_2-n)

    else:
        # 짝수인 경우
        count_2_3 = count_2
        m_2_3 = m_1
        # 나누기 2 연산 이후 +1 연산으로 가는 경우
        m_2_3_1 = m_2_3
        m_2_3_1 //= 2
        count_2_3_1 = count_2_3
        count_2_3_1 += 1 + (n-m_2_3_1)
        # -1연산으로만 가는 경우
        m_2_3_2 = m_2_3
        count_2_3_2 = count_2_3
        count_2_3_2 += (m_2_3-n)

elif m % 2 == 0 and m > n*2:
    