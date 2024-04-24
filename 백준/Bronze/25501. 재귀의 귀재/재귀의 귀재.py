N = int(input())

for _ in range(N):
    s = input()

    def recursion(s, l, r):
        recursion.counter += 1
        if l >= r: return 1
        elif s[l] != s[r]: return 0
        else: return recursion(s, l+1, r-1)
    
    def isPalindrome(s):
        recursion.counter = 0
        result = recursion(s, 0, len(s)-1)
        return result, recursion.counter

    result, recursion_count = isPalindrome(s)
    print(result, recursion_count)