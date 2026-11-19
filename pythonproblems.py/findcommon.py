# # Finding the common numbers without duplicate
# def find_common(numbers1, numbers2):
#     list1 = []
#     for number in numbers1:
#         if number not in list1:
#             list1.append(number)

#     list2 = []
#     for number in numbers2:
#         if number not in list2:
#             list2.append(number)

#     new_list = []
#     for number in list1:
#         for numbers in list2:
#             if number == numbers:
#                 new_list.append(number)
#     return new_list


# print(find_common([3, 1, 4, 3, 5], [4, 4, 3, 6, 1]))



# Calculating the row sum of a matrix

# def row_sums(matrix):
#     total_row = []
#     for rows in matrix:
#         total = 0
#         for number in rows:
#             total += number
#         total_row.append(total)
#     return total_row


# print(row_sums([[1, 2, 3], [4, 5], [6, 7, 8]]))


# Calculating the times target appears in a matrix
# def count_value(matrix, target):
#     count = 0
#     for rows in matrix:
        
#         for number in rows:
#             if number == target:
#                 count += 1
#     return count

# print(count_value([[1, 2, 3], [2, 4], [2, 5, 2]], 2))
# print(count_value([[1, 3], [4, 5]], 2))

# Transpose a matrix
def transpose(matrix):
    new_matrix = []
    
    for i in range(len(matrix[0])):
        new_row = []
        for rows in matrix:
            new_num = rows[i]
        
            new_row.append(new_num)
        new_matrix.append(new_row)   
    return new_matrix


print(transpose([[1, 2, 3], [4, 5, 6]]))
print(transpose([[2, 4], [6, 8], [10, 12]]))