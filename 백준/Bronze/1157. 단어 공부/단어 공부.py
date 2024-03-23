# 대소문자를 구분하지 않고 입력 받은 단어를 소문자로 변환
word = input().lower()

# 각 알파벳이 등장한 횟수를 저장할 딕셔너리 생성
count_dict = {}

# 각 알파벳이 등장한 횟수를 세기
for char in word:
    if char.isalpha():
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

# 가장 많이 등장한 알파벳 찾기
max_count = max(count_dict.values())
max_chars = [char for char, count in count_dict.items() if count == max_count]

# 출력
if len(max_chars) > 1:
    print('?')
else:
    print(max_chars[0].upper())