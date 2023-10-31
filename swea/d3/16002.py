T = int(input())

def solve(n):
    x = 2
    y = n + 2

    while not (is_composite(x) and is_composite(y)):
        x += 1
        y += 1

    return x, y

def is_composite(n):
    if n == 2:
        return False
    for i in range(3, int(n ** 0.5)+1, 2):
        if n % i == 0:
            return True
    return False

for i in range(1 , T+1):
    n = int(input())
    x, y = solve(n)
    print('{}{} {} {}'.format('#', i, x, y))
        
    



    
    
#합성수 판단
#