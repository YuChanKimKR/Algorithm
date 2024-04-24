N = int(input())
dic = {0:0, 1:1}

def fibonacci(N):
    if N in dic:
        return dic[N]
    return fibonacci(N-1) + fibonacci(N-2)

print(fibonacci(N))