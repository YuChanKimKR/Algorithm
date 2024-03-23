def is_palindrome(word):
    # 슬라이싱 이용하기
    return word == word[::-1]

# 입력 받기
word = input()

# 주어진 단어가 팰린드롬인지 여부를 확인하고 결과 출력
if is_palindrome(word):
    print(1)
else:
    print(0)