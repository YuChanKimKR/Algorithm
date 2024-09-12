def solve(s):
    op = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    res = []
    stk = []
    
    for c in s:
        if c.isalpha():
            res.append(c)
        elif c == '(':
            stk.append(c)
        elif c == ')':
            while stk and stk[-1] != '(':
                res.append(stk.pop())
            stk.pop()
        else:
            while stk and op[stk[-1]] >= op[c]:
                res.append(stk.pop())
            stk.append(c)
    
    while stk:
        res.append(stk.pop())
    
    return ''.join(res)

s = input().strip()
print(solve(s))