def draw(n):
    if n == 3:
        return ["***", "* *", "***"]
    
    sub = draw(n // 3)
    res = []

    for i in range(n):
        if (i // (n // 3)) % 3 == 1:
            res.append(sub[i % (n // 3)] + ' ' * (n // 3) + sub[i % (n // 3)])
        else:
            res.append(sub[i % (n // 3)] * 3)

    return res

n = int(input())
result = draw(n)
for line in result:
    print(line)