n, m = map(int, input().split())
arr = []

for i in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)

cnt = 0
money = m

for coin in arr:
    if money >= coin:
        cnt += money // coin
        money %= coin

print(cnt)