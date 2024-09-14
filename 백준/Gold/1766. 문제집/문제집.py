import heapq
import sys
input = sys.stdin.readline

def topology_sort(N, M, graph, in_degree):
    result = []
    heap = []

    # 진입 차수가 0인 문제들을 우선순위 큐에 넣는다
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            heapq.heappush(heap, i)
    
    while heap:
        # 가장 작은 문제 번호를 꺼낸다
        current = heapq.heappop(heap)
        result.append(current)

        # 현재 문제와 연결된 문제들의 진입 차수를 줄인다
        for next_problem in graph[current]:
            in_degree[next_problem] -= 1
            # 진입 차수가 0이 되면 큐에 넣는다
            if in_degree[next_problem] == 0:
                heapq.heappush(heap, next_problem)
    
    return result

# 입력 받기
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)

# 그래프와 진입 차수 정보 구축
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    in_degree[B] += 1

# 위상 정렬 수행
result = topology_sort(N, M, graph, in_degree)

# 결과 출력
print(' '.join(map(str, result)))