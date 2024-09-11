N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

used = [False] * N
res = []
tmp = []

def backtrack():
    if len(tmp) == M:
        print(' '.join(map(str, tmp)))
        return

    prev = -1
    for i in range(N):
        if not used[i] and nums[i] != prev:
            used[i] = True
            tmp.append(nums[i])
            prev = nums[i]
            backtrack()
            tmp.pop()
            used[i] = False

backtrack()