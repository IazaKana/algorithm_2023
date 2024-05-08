n = list(map(str, input()))

n.sort(reverse = True)
print(''.join(n))

# join함수 - 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 반환하는 함수