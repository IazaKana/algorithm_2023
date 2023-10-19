from collections import defaultdict, Counter
# def solution(s):
#     odd = 0
#     sH = Counter(s)
#     for key in sH:
#         if sH[key] % 2 == 1:
#             odd += 1
#     return odd <= 1

# print(solution("abacbaa"))
# print(solution("abaaceeffkckbaa"))
# print(solution("abcabbcc"))
# print(solution("sgsgsgabaaaecececekefefkccckbsgaaffsgsg"))
# print(solution("aabcefagcefbcabbcc"))

def solution(s):
    odd = 0
    nH = defaultdict(int)
    for i in s:
        nH[i] += 1
    print(nH)
    for key in nH:
        if nH[key] % 2 == 1:
            odd += 1
    return odd <= 1

print(solution("abacbaa"))
print(solution("abaaceeffkckbaa"))
print(solution("abcabbcc"))
print(solution("sgsgsgabaaaecececekefefkccckbsgaaffsgsg"))
print(solution("aabcefagcefbcabbcc"))

# defaultdict 사용법
# animals = ['dog', 'cat', 'rabbit', 'tiger', 'cat', 'cat', 'rabbit']
# dic = {}

# for animal in animals:
#     # key가 있다면 1 증가
#     if animal in dic.keys():
#         dic[animal] += 1
#     # key가 없다면 1로 초기화
#     else:
#         dic[animal] = 1