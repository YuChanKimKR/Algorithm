N = int(input())  # 과목의 개수 입력
scores = list(map(int, input().split()))  # 세준이의 현재 성적 입력

# 최댓값 찾기
max_score = max(scores)

# 새로운 성적 계산 후 리스트에 저장
new_scores = [(score / max_score) * 100 for score in scores]

# 새로운 성적들의 평균 계산
average = sum(new_scores) / N

# 결과 출력
print(average)