numbers = list(map(int, input().split()))  # 고유번호의 처음 5자리 숫자를 리스트로 입력 받음

# 검증수 계산
verification_sum = sum(num ** 2 for num in numbers) % 10

print(verification_sum)