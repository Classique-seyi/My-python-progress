# def first_duplicate(numbers):
#     new_list = []
#     for number in numbers:
#         if number in new_list:
#             return number
#         else:
#             new_list.append(number)
#     return None

# print(first_duplicate([3, 1, 4, 1, 3]))
# print(first_duplicate([5, 2, 5, 2]))
# print(first_duplicate([1, 2, 3, 4]))

#Counting words in a sentence 
def count_words(sentence):
    words = sentence.split()

    count = 0
    for word in words:
        count += 1
    return count

# Getting the average word length in a sentence
def average_word_length(sentence):
    length = count_words(sentence)
    words = sentence.split()

    count = 0
    for word in words:
        count += len(word)
    try:
        average = count / length
    except ZeroDivisionError:
        return None
    return average

print(count_words("I love python"))
print(count_words(""))
print(average_word_length("I love python"))
print(average_word_length(""))