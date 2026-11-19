def find_missing(numbers):
    if not numbers:
        return []

    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    
    new_total = 0
    n = len(numbers) + 1
    for i in range(1, n+1):
        new_total += i
    missing = new_total - total
    return missing


# print(find_missing([1, 2, 3, 5]))
# print(find_missing([1, 2, 4, 5]))


def remove_duplicates(numbers):
    num_list = []
    for num in numbers:
        if num not in num_list:
            num_list.append(num)
    return num_list


# print(remove_duplicates([1, 2, 2, 3, 1]))
# print(remove_duplicates([4, 4, 4]))
# print(remove_duplicates([1, 2, 3]))


# calculating the sum of even numbers in a list
def get_even_numbers(numbers):
    num_list = []
    if not numbers:
        return []
    for num in numbers:
        if num%2 == 0:
            num_list.append(num)
    return num_list

def sum_even_numbers(numbers):
    number = get_even_numbers(numbers)

    total = 0
    for num in number:
        total += num
    return total


print(get_even_numbers([1, 2, 2, 4, 3, 5, 6, 7, 10]))
print(sum_even_numbers([1, 2, 2, 4, 3, 5, 6, 7, 10]))
