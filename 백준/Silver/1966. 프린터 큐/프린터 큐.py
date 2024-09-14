from collections import deque

def printer_queue(N, M, priorities):
    queue = deque([(i, priorities[i]) for i in range(N)])  # (문서 위치, 중요도)
    count = 0  # 인쇄 순서
    
    while queue:
        current = queue.popleft()
        # 현재 문서의 중요도보다 높은 문서가 뒤에 있으면 다시 큐에 삽입
        if any(current[1] < doc[1] for doc in queue):
            queue.append(current)
        else:
            # 현재 문서 출력
            count += 1
            if current[0] == M:  # 목표 문서가 인쇄된 경우
                return count

# 입력 처리
test_cases = int(input())

for _ in range(test_cases):
    N, M = map(int, input().split())  # 문서의 개수 N, 인덱스 M
    priorities = list(map(int, input().split()))  # 문서의 중요도
    print(printer_queue(N, M, priorities))
