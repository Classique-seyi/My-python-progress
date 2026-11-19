def get_even_numbers(numbers):
    num_list = []
    for number in numbers:
        if number%2 == 0:
            num_list.append(number)
    return num_list


def get_squares(numbers):
    num_list = get_even_numbers(numbers)
    new_list = []

    for number in num_list:
        square = number ** 2
        new_list.append(square)

    return new_list

def sum_even_squares(numbers):
    even_list = get_squares(numbers)

    total = 0
    for number in even_list:
        total += number
    return total



print(get_even_numbers([1, 2, 3, 4, 5, 6]))
print(get_squares([1, 2, 3, 4, 5, 6]))
print(sum_even_squares([1, 2, 3, 4, 5, 6]))