from collections import Counter
def solution(s):
    answer = False
    nH = Counter(s)
    n = 0
    for key in nH:
        if nH[key] % 2 == 1:
            n += 1
    
    if n % 2 == 0:
        answer = False
    else:
        answer = True
    
    return answer     
                      
print(solution("abacbaa"))
print(solution("abaaceeffkckbaa"))
print(solution("abcabbcc"))
print(solution("sgsgsgabaaaecececekefefkccckbsgaaffsgsg"))
print(solution("aabcefagcefbcabbcc"))

def solution(s):
    sH = Counter(s)
    odd = 0
    for key in sH:
        if sH[key] % 2 == 1:
            odd += 1
    return odd <= 1  