def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(key=lambda v : v*3, reverse=True)
    
    return str(int("".join(numbers)))

#문자열 sort정렬