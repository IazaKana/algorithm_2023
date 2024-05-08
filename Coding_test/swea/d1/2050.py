# n = str(input())

# for i in range(len(n)):
#     a = ord(n[i])
#     print(int(a) - 64)

n = str(input())

print(*[int(ord(c) - 64) for c in n])


# n = str(input())

# print(''.join([chr(int(ord(c) - 64)) for c in n]))

# 축약문 숙지

# 리스트 요소 한번에 출력하기: print(*arr)