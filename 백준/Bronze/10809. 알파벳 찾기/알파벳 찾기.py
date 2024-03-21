S = input()
alphabet_indices = [-1] * 26

for idx, char in enumerate(S):
    index = ord(char.lower()) - ord('a')
    if 0 <= index < 26 and alphabet_indices[index] == -1:
        alphabet_indices[index] = idx

print(*alphabet_indices)