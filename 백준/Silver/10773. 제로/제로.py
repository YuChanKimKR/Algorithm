import sys
input = sys.stdin.readline

N = int(input())
stack = list()

def cal():
    if ans == 0:
        stack.pop()
    
    if ans != 0:
        stack.append(ans)


for _ in range(N):
    ans = int(input())
    cal()

ans = sum(stack)
print(ans)