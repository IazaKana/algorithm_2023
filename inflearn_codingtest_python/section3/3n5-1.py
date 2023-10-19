from collections import defaultdict, Counter
def solution(s):
    answer = 0
    a = 0
    nH = Counter(s)
    for key in nH:
        if nH[key] % 2 == 0:
            answer += nH[key]
        else:
            a = max(a, nH[key])
            
    answer += a
    return answer

print(solution("abcbbbccaaeee"))
print(solution("aabbccddee"))
print(solution("fgfgabtetaaaetytceefcecekefefkccckbsgaafffg"))
print(solution("aabcefagcefbcabbcc"))
print(solution("abcbbbccaa"))

def solution(s):
    sH = Counter(s)
    odd = 0
    for key in sH:
        if sH[key] % 2 == 1:
            odd += 1

    return len(s) - odd + 1 if odd > 0 else len(s)