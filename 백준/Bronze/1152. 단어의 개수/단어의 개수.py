# 입력 문자열을 공백을 기준으로 분리하여 단어들의 리스트를 만든 후, 리스트의 길이를 출력
input_str = input().strip()  # 입력 문자열을 받고 양쪽 공백 제거
word_list = input_str.split()  # 공백을 기준으로 문자열을 분리하여 단어 리스트 생성
print(len(word_list))  # 단어 리스트의 길이 출력