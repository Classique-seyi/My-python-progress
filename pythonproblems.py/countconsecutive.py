# Count repeated characters
# def count_repeats(text):
#     text_dict = {}
#     for char in text:
#         if char in text_dict:
#             text_dict[char] += 1
#         else:
#             text_dict[char] = 1

#     count = 0
#     for char in text_dict:
#         if text_dict[char] > 1:
#             count += 1
#     return count


# count consecutive characters
# def count_repeats(text):
#     count = 0
#     for i in range(len(text)-1):
#         if (i == 0 or text[i] != text[i-1]) and text[i] == text[i+1]:
#             count += 1
#     return count


# print(count_repeats("abbbaccc"))
# print(count_repeats("aabbcc"))
# print(count_repeats("abc"))     
# print(count_repeats("mississippi"))


# Counting the longest increasing sequence
def longest_increasing(numbers):
    if not numbers:
        return 0
    current = 1
    longest = 1
    for i in range(len(numbers)-1):
        if numbers[i] < numbers[i+1]:
            current += 1
        else:
            current = 1
        if current > longest:
            longest = current
    return longest

print(longest_increasing([1, 2, 3, 1, 2]))
print(longest_increasing([5, 4, 3, 2]))
print(longest_increasing([1, 3, 2, 4, 5]))
print(longest_increasing([7, 7, 8, 9]))
print(longest_increasing([]))
print(longest_increasing([5]))  


