N = int(input())

for i in range(N // 5, -1, -1):
    m = N - i * 5
    if m % 3 == 0:
        print(i + m // 3)
        break
else:
    print(-1)