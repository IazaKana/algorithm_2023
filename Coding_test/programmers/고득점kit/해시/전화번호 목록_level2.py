from collections import Counter

def solution(phone_book):
    
    a = Counter(phone_book)
    
    for x in a:
        ab = ''
        for y in x:
            ab += y
            if ab in a and ab != x:
                return False
    
    return True