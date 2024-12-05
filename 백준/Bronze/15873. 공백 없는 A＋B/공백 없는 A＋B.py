N = list(map(int, input()))

if len(N) == 2:
    result = sum(N)

if len(N) == 3:
    result = sum(N) + 9

if len(N) == 4:
    result = 20

print(result)