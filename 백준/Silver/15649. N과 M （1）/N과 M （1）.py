N, M = map(int, input().split())
s = []
visited = [False] * (N+1)

def search():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    for i in range(1, N+1):
        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        search()
        s.pop()
        visited[i] = False

search()