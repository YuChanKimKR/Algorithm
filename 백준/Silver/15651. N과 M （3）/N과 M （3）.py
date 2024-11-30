N, M = map(int, input().split())
arr = []

def backtracking(start):
    if len(arr) == M:
        print(" ".join(map(str, arr)))
        return
        
    for i in range(1, N+1):
        arr.append(i)
        backtracking(i+1)
        arr.pop()

backtracking(1)