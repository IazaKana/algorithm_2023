m = ['+' for _ in range(5)]

for i in range(len(m)):
    m[i] = '#'
    print(''.join(m))
    m[i] = '+'


#파이썬에서 문자열은 불변 객체
#join 함수는 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 반환하는 함수

# m = '+++++'

# m_list = list(m)
# m_list[0] = '#'

# m = ''.join(m_list)

# print(m)