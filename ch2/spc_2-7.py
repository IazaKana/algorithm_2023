# 자료형을 정하지 않은 리스트 원소 확인하기

x = [15, 64, 7, 3.14, [32, 55], 'ABC']
for i in range(len(X)):
    print(f'x[{i}] = {x[i]}')

# 얕은복사 - 리스트 안의 모든 원소가 참조하는 곳까지 복사
# 깊은복사 - 리스트의 원소뿐만 아니라 구성 원소도 복사