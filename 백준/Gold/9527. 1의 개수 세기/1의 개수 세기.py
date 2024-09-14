def counting(x):
    if x == 0:
        return 0
    
    count = 0
    bit = 1
    
    while bit <= x:
        quotient = (x + 1) // (bit * 2)
        remainder = (x + 1) % (bit * 2)
        
        count += quotient * bit
        count += max(0, remainder - bit)
        
        bit *= 2
    
    return count

A, B = map(int, input().split())
result = counting(B) - counting(A - 1)
print(result)