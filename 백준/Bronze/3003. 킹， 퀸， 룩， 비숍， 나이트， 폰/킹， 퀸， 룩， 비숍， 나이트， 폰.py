def calculate_operations(numbers):
    target_numbers = [1, 1, 2, 2, 2, 8]  # 주어진 예시 [0, 1, 2, 2, 2, 7]에 대한 목표 숫자 배열

    operations = [0] * 6  # 초기 연산 횟수 배열 초기화

    for i in range(6):
        operations[i] = target_numbers[i] - numbers[i]  # 목표 숫자와 입력된 숫자의 차이 계산

    return operations

# 입력 받기
input_numbers = list(map(int, input().split()))

# 연산 횟수 계산
result = calculate_operations(input_numbers)

# 결과 출력
print(*result)