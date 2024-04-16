N, K = map(int, input().split())
coins = []

for _ in range(N):
    coins.append(int(input()))

coins = list(reversed(coins))
count = 0

for coin in coins:
    if K == 0:  # K원을 모두 만들었으면 반복 종료
        break
    if coin <= K:
        count += K // coin
        K %= coin

print(count)