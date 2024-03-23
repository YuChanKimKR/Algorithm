# 그룹 단어 판별 함수
def is_group_word(word):
    visited = []  # 이미 방문한 문자를 저장하기 위한 리스트
    prev_char = None  # 이전 문자를 저장하기 위한 변수
    for char in word:
        if char in visited:  # 이미 방문한 문자인 경우
            if char != prev_char:  # 현재 문자가 바로 이전 문자와 다르다면 그룹 단어가 아님
                return False
        else:  # 처음 방문한 문자인 경우
            visited.append(char)  # 방문한 문자로 표시
        prev_char = char  # 이전 문자를 현재 문자로 업데이트
    return True  # 모든 문자를 확인했을 때 그룹 단어임을 반환

# 단어의 개수 입력 받기
N = int(input())

# 그룹 단어의 개수 카운트 변수 초기화
group_word_count = 0

# 단어들을 입력받고 그룹 단어인지를 판별하여 카운트
for _ in range(N):
    word = input()
    if is_group_word(word):
        group_word_count += 1

# 결과 출력
print(group_word_count)