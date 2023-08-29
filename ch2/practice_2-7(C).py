#10진수 정숫값을 입력받아 2~36진수로 변환하여 출력하기

def card_conv(x: int, r: int) -> str:  #정숫값 x를 r진수로 변환한 뒤 그 수를 나타내는 문자열을 반환

    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = len(str(x))

    print(f'{r:2} | {x:{n}d}')  #이 줄은 정숫값 x를 r진수로 변환한 뒤 그 수를 나타내는 문자열을 출력합니다. f 문자열 포맷팅을 사용하여 정수 r을 2자리 문자열로 출력하고, x를 n자리 문자열로 출력합니다
    while x > 0:
        print('  +' + (n + 2) * '-')
        if x // r:
            print(f'{r:2} | {x // r:{n}d} --- {x % r}')
        else:
            print(f'     {x // r:[n]d} --- {x % r}')
        d += dchar [x % r]
        x //= r

    return d[::-1]

if __name__ == '__main__':
    print('10진수를 n진수로 변환합니다.')

    while True:
        while True:
            no = int(input('변환할 값으로 음이 아닌 정수를 입력세요.: '))
            if no > 0:
                break

        while True:
            cd = int(input('어떤 진수로 변환할까요?: '))
            if 2 <= cd <= 36:
                break
            
        print(f'{cd}진수로는 {card_conv(no, cd)}입니다.')

        retry = input("한 번 더 변환할까요?(Y / N): ")
        if retry in {'N', 'n'}:
            break