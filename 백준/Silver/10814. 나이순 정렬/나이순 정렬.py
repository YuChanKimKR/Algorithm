N = int(input())
info_list = []

for _ in range(N):
    info = input().split()
    info_list.append(info)

info_list.sort(key=lambda x: (int(x[0])))

for info in info_list:
    print(info[0], info[1])