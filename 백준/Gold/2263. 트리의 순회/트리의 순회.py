import sys
sys.setrecursionlimit(10**6)

def solve(in_s, in_e, post_s, post_e):
    if in_s > in_e:
        return
    root = post[post_e]
    pre.append(root)
    idx = in_map[root]
    left = idx - in_s
    solve(in_s, idx - 1, post_s, post_s + left - 1)
    solve(idx + 1, in_e, post_s + left, post_e - 1)

n = int(input())
inorder = list(map(int, input().split()))
post = list(map(int, input().split()))

in_map = {v: i for i, v in enumerate(inorder)}
pre = []

solve(0, n - 1, 0, n - 1)

print(' '.join(map(str, pre)))