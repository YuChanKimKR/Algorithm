N = int(input())
numbers = list(map(int, input().split()))

sorted_numbers = sorted(list(set(numbers)))

coordinate_dict = {value: index for index, value in enumerate(sorted_numbers)}

compressed_coordinates = [coordinate_dict[number] for number in numbers]

print(*compressed_coordinates)