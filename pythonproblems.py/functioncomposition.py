# def count_words(sentence):
#     words = sentence.split()

#     count = 0
#     for word in words:
#         count += 1
#     return count

# def longest_word_length(sentence):
#     if not sentence:
#         return 0
#     count = count_words(sentence)

#     words = sentence.split()
#     longest = words[0]
#     for word in words:
#         if len(word) > len(longest):
#             longest = word

#     if count < 2:
#         return 0
#     else:
#         return len(longest)


# print(longest_word_length("I love programming"))
# print(longest_word_length("Hello there"))
# print(longest_word_length("Hello"))
# print(longest_word_length(""))
# print(count_words(""))



# Finding the second smallest uniques number
def second_smallest(numbers):
    unique = []
    for number in numbers:
        if number not in unique:
            unique.append(number)

    smallest = unique[0]
    
    for number in unique:
        if number < smallest:
            smallest = number

    unique.remove(smallest)
    second_smallest = unique[0]
    for number in unique:
        if number < second_smallest:
            second_smallest = number
    return second_smallest

print(second_smallest([4, 1, 7, 2, 1]))
print(second_smallest([8, 3, 5, 3, 9]))
print(second_smallest([2, 2, 6, 6, 9]))

    

