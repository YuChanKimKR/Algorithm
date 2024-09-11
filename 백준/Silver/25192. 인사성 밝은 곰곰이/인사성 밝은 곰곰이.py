n = int(input())
count = 0
users = {}

for _ in range(n):
    log = input().strip()
    
    if log == "ENTER":
        users.clear()
    else:
        if log not in users:
            count += 1
            users[log] = True

print(count)