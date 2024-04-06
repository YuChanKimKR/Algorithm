n = int(input())

dot = 3
inc = 2

for i in range(1, n):
    dot += inc
    inc *= 2

print(dot * dot)