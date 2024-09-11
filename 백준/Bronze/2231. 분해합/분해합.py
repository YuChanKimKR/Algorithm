def find_function(N):
    for M in range(1, N):
        
        sum1 = M + sum(map(int, str(M)))
        if sum1 == N:
            return M
    return 0

N = int(input())
print(find_function(N))