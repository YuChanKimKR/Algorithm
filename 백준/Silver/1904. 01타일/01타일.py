import sys
input = sys.stdin.readline

N = int(input())
memo = [-1] * 1000001

def search(N):
    memo[1] = 1
    memo[2] = 2
    memo[3] = 3
    memo[4] = 5

    if N == 1:
        return 1

    if N == 2:
        return 2

    for i in range(3, N+1):
        memo[i] = (memo[i - 1] + memo[i - 2]) % 15746
    return memo[N]

print(search(N))