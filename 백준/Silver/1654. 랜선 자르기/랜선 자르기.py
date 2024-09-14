import sys
input = sys.stdin.readline

# 입력 처리
K, N = map(int, input().split())
lan_cables = [int(input()) for _ in range(K)]

# 이분 탐색 설정
start, end = 1, max(lan_cables)

# 이분 탐색
while start <= end:
    mid = (start + end) // 2  # 중간 값(랜선 길이 후보)
    count = sum(lan // mid for lan in lan_cables)  # 중간 길이로 잘랐을 때의 랜선 개수
    
    if count >= N:  # 필요한 랜선 개수 이상을 만들 수 있으면 길이를 늘림
        start = mid + 1
    else:  # 랜선 개수가 부족하면 길이를 줄임
        end = mid - 1

# 최종적으로 end는 N개 이상의 랜선을 만들 수 있는 최대 길이
print(end)
