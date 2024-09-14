n = int(input())
sequence = [int(input()) for _ in range(n)]

stack = []
result = []
current = 1
possible = True

for num in sequence:
    # 스택에 들어갈 숫자가 아직 목표 숫자보다 작으면 push
    while current <= num:
        stack.append(current)
        result.append('+')
        current += 1
    
    # 스택의 가장 위의 숫자가 목표 숫자와 같으면 pop
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        possible = False
        break

if possible:
    print('\n'.join(result))
else:
    print('NO')
