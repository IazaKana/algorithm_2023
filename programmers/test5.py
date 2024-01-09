from itertools import combinations, permutations

numbers = [4, 10, 4]

numbers = list(map(str, numbers))
print(numbers)
numbers.sort(key = lambda x : x*3, reverse = True)
