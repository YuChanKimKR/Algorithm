def mod(A, B, C):
    if B == 0:
        return 1
    half = mod(A, B // 2, C)
    half = (half * half) % C
    if B % 2 == 0:
        return half
    else:
        return (half * A) % C

A, B, C = map(int, input().split())
print(mod(A, B, C))