def f(a, b):
    c = 0
    while b > a:
        if b % 10 == 1:
            b //= 10
        elif b % 2 == 0:
            b //= 2
        else:
            return -1
        c += 1
    return c + 1 if b == a else -1

a, b = map(int, input().split())
print(f(a, b))