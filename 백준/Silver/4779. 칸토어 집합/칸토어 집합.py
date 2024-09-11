import sys
input = sys.stdin.read

def cantor_set(n):
    if n == 0:
        return "-"
    else:
        prev = cantor_set(n - 1)
        return prev + " " * len(prev) + prev

data = input().split()

for n in data:
    n = int(n)
    print(cantor_set(n))
