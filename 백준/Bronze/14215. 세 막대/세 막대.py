a, b, c = map(int, input().split())

sides = [a, b, c]
sides.sort()

if sides[0] + sides[1] > sides[2]:
    print(sum(sides))
else:
    print(2 * (sides[0] + sides[1]) - 1)