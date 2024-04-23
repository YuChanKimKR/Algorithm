def backtrack(N, M, depth, result, visited):
    if depth == M:  # 수열의 길이가 M에 도달한 경우
        print(' '.join(map(str, result)))  # 현재까지 선택된 수열 출력
        return
    
    for i in range(1, N+1):
        if not visited[i]:  # 아직 방문하지 않은 숫자인 경우
            if not result or i > result[-1]:  # 오름차순인 경우에만 선택
                visited[i] = True  # 숫자 방문 표시
                result.append(i)  # 수열에 숫자 추가
                backtrack(N, M, depth+1, result, visited)  # 다음 숫자 선택
                result.pop()  # 백트래킹: 선택한 숫자 제거
                visited[i] = False  # 숫자 방문 표시 해제

N, M = map(int, input().split())  # 자연수 N과 M 입력 받기
backtrack(N, M, 0, [], [False] * (N+1))  # 백트래킹 알고리즘 호출