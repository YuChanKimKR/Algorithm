def convert_to_decimal(n, base):
    decimal = 0
    for digit in n:
        if digit.isdigit():
            value = int(digit)
        else:
            value = ord(digit) - ord('A') + 10
        decimal = decimal * base + value
    return decimal

N, B = input().split()
B = int(B)
decimal_value = convert_to_decimal(N, B)
print(decimal_value)