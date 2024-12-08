N = int(input())

string1 = set([input() for _ in range(0, N)])
strings = sorted(string1)

for i in range(1, 51):
    for j in range(0, len(strings)):
        if len(strings[j]) == i:
            print(strings[j])