N = int(input())

values = [int(input()) for _ in range(N)]

values.sort()

for number in values:
    print(number)