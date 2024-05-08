from collections import Counter
def solution(s):
    s = Counter(s)
    cnt = 0
    result = True
    for x in s:
        if s[x] % 2 == 1:
            cnt += 1
            if cnt == 2:
                result = False
    
    return result

print(solution("abacbaa"))
print(solution("abaaceeffkckbaa"))
print(solution("abcabbcc"))
print(solution("sgsgsgabaaaecececekefefkccckbsgaaffsgsg"))
print(solution("aabcefagcefbcabbcc"))