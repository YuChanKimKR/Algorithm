import sys
sys.setrecursionlimit(10**6)

N = int(input())

def factorial(N):
    if N < 2:
        return 1
    return N * factorial(N-1)

print(factorial(N))