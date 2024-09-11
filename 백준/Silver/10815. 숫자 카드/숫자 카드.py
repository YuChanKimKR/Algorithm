N = int(input())
cards = set(map(int, input().split()))

M = int(input())
checkd = list(map(int, input().split()))

result = []
for card in checkd:
    if card in cards:
        result.append(1)
    else:
        result.append(0)

print(" ".join(map(str, result)))