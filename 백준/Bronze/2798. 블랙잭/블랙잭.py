# 카드의 개수 N, 목표 합 M 입력 받기
N, M = map(int, input().split())

# 카드에 쓰여 있는 수 입력 받기
cards = list(map(int, input().split()))

# 가장 가까운 합 초기화
closest_sum = 0

# 카드들을 정렬
cards.sort()

# 가능한 카드 조합을 확인하여 가장 가까운 합 찾기
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            card_sum = cards[i] + cards[j] + cards[k]
            # 현재 합이 목표 합 M보다 작고, 기존의 가장 가까운 합보다 크다면 갱신
            if card_sum <= M and card_sum > closest_sum:
                closest_sum = card_sum

# 결과 출력
print(closest_sum)