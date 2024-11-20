N = int(input())

memo = [-1] * (N + 1)
count = 0 

def fibo(N, memo):
    global count
    count += 1
    
    if N <= 1:
        return N
    if memo[N] != -1:
        return memo[N]
        
    memo[N] = fibo(N - 1, memo) + fibo(N - 2, memo)
    return memo[N]

print(fibo(N, memo), (count // 2) - 1)