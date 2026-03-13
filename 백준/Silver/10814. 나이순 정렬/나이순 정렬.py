n = int(input())

data = [None] * n

for i in range(n):
    row = input().split()
    age = int(row[0])
    name = row[1]

    data[i] = (age, name, i)

data.sort(key = lambda x: (x[0], x[2]) )

for person in data:
    print(person[0], person[1])