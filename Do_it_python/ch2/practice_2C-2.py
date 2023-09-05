#리스트의 모든 원소를 enumerate() 함수로 스캔하기

x = ['A', 'B', 'C', 'D']

for i, name in enumerate(x):
    print(f'x[{i}] = {name}')

#인덱스와 원소를 짝지어 enumerate() 함수로 반복해서 꺼냄
#튜플은 리스트로 작성한 x = []를 x = ()로 수정하는 것만으로 스캔할 수 있음