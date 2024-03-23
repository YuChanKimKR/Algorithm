word = input()

# 크로아티아 알파벳에 해당하는 문자열들을 리스트로 저장
croatian_alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# 크로아티아 알파벳 개수를 카운트할 변수 초기화
count = 0

# 주어진 단어를 순회하면서 크로아티아 알파벳을 찾고 개수를 카운트
idx = 0
while idx < len(word):
    found = False
    for alphabet in croatian_alphabets:
        if word[idx:idx+len(alphabet)] == alphabet:
            count += 1
            idx += len(alphabet)
            found = True
            break
    if not found:
        count += 1
        idx += 1

# 결과 출력
print(count)