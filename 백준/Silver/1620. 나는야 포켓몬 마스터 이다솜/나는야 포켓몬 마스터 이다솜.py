# 입력 받기
N, M = map(int, input().split())

# 포켓몬 이름을 저장할 리스트 및 번호로 포켓몬 이름을 찾기 위한 딕셔너리
pokemon_list = []
name_to_number = {}

# 포켓몬 이름 입력 받기
for i in range(1, N + 1):
    name = input().strip()
    pokemon_list.append(name)
    name_to_number[name] = i

# 문제 입력 및 처리
results = []

for _ in range(M):
    query = input().strip()
    if query.isdigit():
        # 입력이 숫자인 경우 포켓몬 이름 출력
        index = int(query)
        results.append(pokemon_list[index - 1])
    else:
        # 입력이 문자인 경우 포켓몬 번호 출력
        results.append(str(name_to_number[query]))

# 결과 출력
for result in results:
    print(result)