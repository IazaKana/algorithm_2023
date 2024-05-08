import math
from itertools import permutations

def is_prime_number(x):
    if x < 2:
        return False
    
    for i in range(2, x):
        if x % i == 0:
            return False
    
    return True

def solution(numbers):
    
#     A = ['x'] * (10000001)
    answer = 0
    
#     for i in range(2, 1000001):
#         A[i] = i
    
#     for i in range(2, int(math.sqrt(100000)) + 1):
#         for j in range(i + i, 1000001, i):
#             A[j] = 'x'
    
    N = [x for x in numbers]
    P = []
    for i in range(1, len(numbers) + 1):
        P += list(permutations(N, i))
    new_N = list(set([int(("").join(x)) for x in P]))
    
    for i in new_N:
        if is_prime_number(i) == True:
            answer += 1
    
    # for i in new_N:
    #     if i in A:
    #         answer += 1
    
    
    return answer