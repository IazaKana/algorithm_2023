def gcd(A, B):
    if B == 0:
        return A
    else:
        return gcd(B, A%B)

A, B = map(int, input().split())

print(str(1) * gcd(A, B))