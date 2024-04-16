N = int(input())

meetings = []

for _ in range(N):
    start, end = map(int, input().split())
    meetings.append((start, end))

meetings.sort(key=lambda x: (x[1], x[0]))

max = 0
end_time = 0

for meeting in meetings:
    start, end = meeting
    if start >= end_time:
        max += 1
        end_time = end

print(max)