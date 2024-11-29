N, M = map(int, input().split())
answer = []

def backtracking():
    if len(answer) == M:
        print(" ".join(map(str, answer)))
        return
    
    for i in range(1, N+1):
        if i not in answer:
            answer.append(i)
            backtracking()
            answer.pop()

backtracking()