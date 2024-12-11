from collections import deque
N = int(input())

def check():
    t = 0
    while len(dq) > 0:
        if dq.popleft() == '(':
            t += 1
        else:
            t -= 1
            
        if t < 0:
            print("NO")
            return
        
    if t == 0:
        print("YES")
    else:
        print("NO")
    return
        
for _ in range(0, N):
    arr = input()
    dq = deque(arr)
    check()