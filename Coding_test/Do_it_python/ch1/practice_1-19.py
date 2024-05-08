# 1~12까지 8을 건너뛰고 출력하기1

for i in range(1, 13):
    if i == 8:
        continue
    print(i, end='')

print()

#비효율적
#숫자가 커지면 1개만 건너뛰기위해 판단을 그 숫자만큼 해야하기 때문
