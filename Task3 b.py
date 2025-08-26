numbers_input = input("Enter numbers separated by commas: ")
numbers_list = numbers_input.split(",")

numbers = []
for num in numbers_list:
    numbers.append(int(num))

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] = frequency[num] + 1
    else:
        frequency[num] = 1

print(frequency)
