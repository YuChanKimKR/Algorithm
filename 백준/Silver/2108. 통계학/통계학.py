import sys
input = sys.stdin.readline

n = int(input().strip())
nums = [int(input().strip()) for _ in range(n)]

total = sum(nums)
print(round(total / n))

nums.sort()
print(nums[n // 2])

from collections import Counter
cnt = Counter(nums).most_common()
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])

print(nums[-1] - nums[0])