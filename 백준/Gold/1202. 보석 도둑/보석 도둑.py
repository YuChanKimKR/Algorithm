import sys
import heapq

input = sys.stdin.readline

# 입력 받기
N, K = map(int, input().split())
jewels = []
bags = []

# 보석 정보 입력
for _ in range(N):
    M, V = map(int, input().split())
    jewels.append((M, V))  # (무게, 가격) 튜플

# 가방 정보 입력
for _ in range(K):
    C = int(input())
    bags.append(C)

# 보석은 무게를 기준으로 오름차순 정렬
jewels.sort()
# 가방도 무게를 기준으로 오름차순 정렬
bags.sort()

# 최대 가격을 저장할 변수
max_value = 0
# 우선순위 큐(최대 힙을 사용하기 위해 음수값으로 삽입)
valid_jewels = []
idx = 0

# 가방을 하나씩 확인하면서, 해당 가방에 넣을 수 있는 보석들을 선택
for bag in bags:
    # 현재 가방에 들어갈 수 있는 보석들을 모두 추가
    while idx < N and jewels[idx][0] <= bag:
        # 힙은 최소 힙이므로, 최대 가격을 구하기 위해 음수로 변환해서 저장
        heapq.heappush(valid_jewels, -jewels[idx][1])
        idx += 1
    
    # 만약 가방에 넣을 수 있는 보석이 있으면, 가장 비싼 보석을 선택
    if valid_jewels:
        max_value += -heapq.heappop(valid_jewels)

# 결과 출력
print(max_value)
