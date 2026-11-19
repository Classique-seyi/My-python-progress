# def second_largest(numbers):
#     if not numbers:
#         return []
#     largest = max(numbers)
#     numbers.remove(largest)
            
#     second_largest = max(numbers)

#     return(second_largest)

# print(second_largest([4, 8, 2, 10, 6]))

# print(second_largest([3, 9, 9, 5, 2]))

# print(second_largest([]))


# Calculating the second largest unique number
def second_largest(numbers):
    unique = []
    for number in numbers:
        if number not in unique:
            unique.append(number)
    
    largest = unique[0]

    for number in unique:
        if number > largest:
            largest = number


    unique.remove(largest)
    second = unique[0]

    for number in unique:
        if number > second:
            second = number

    return second

print(second_largest([4, 1, 7, 3, 7, 5]))
print(second_largest([10, 10, 8, 6]))
print(second_largest([-5, -2, -9]))