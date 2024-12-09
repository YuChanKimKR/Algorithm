import collections
import sys
input = sys.stdin.readline

N = int(input())
arr = list()

for _ in range(N):
    nums = int(input())
    arr.append(nums)

arr.sort()

first = round(sum(arr) / N)
second = arr[(len(arr) // 2)]

d = collections.Counter(arr);
M = max(d.values())
m = 0
for i in range(N):
    if (i==0)|(arr[i-1]!=arr[i]):k=1
    else:k+=1
    if M==k:
        if m:m=arr[i];break
        else:m=arr[i]
            
for i in arr:
    four = max(arr[0], i) - min(arr[0], i)
    
print(first)
print(second)
print(m)
print(four)