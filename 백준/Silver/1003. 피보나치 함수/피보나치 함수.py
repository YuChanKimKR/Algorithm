T = int(input())

zero = {}
one = {}

def fibonacci(N):
    if N == 0:
        zero[N] = 1
        one[N] = 0
        return 0
    elif N == 1:
        zero[N] = 0
        one[N] = 1
        return 1
    else:
        if N not in zero:
            fibonacci(N-1)
            fibonacci(N-2)
            zero[N] = zero[N-1] + zero[N-2]
            one[N] = one[N-1] + one[N-2]
        return zero[N]

for _ in range(T):
    N = int(input())
    fibonacci(N)
    print(zero[N], one[N])