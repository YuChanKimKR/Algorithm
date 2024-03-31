# 다섯 줄의 단어들을 입력받음
words = [input() for _ in range(5)]

max_length = max(len(word) for word in words)  # 가장 긴 단어의 길이를 찾음

result = ''  # 결과를 저장할 문자열

# 각 자리를 세로로 읽음
for i in range(max_length):
    for word in words:
        # 현재 단어의 길이가 현재 위치보다 크다면 해당 위치의 글자를 결과에 추가
        if i < len(word):
            result += word[i]

# 결과 출력
print(result)