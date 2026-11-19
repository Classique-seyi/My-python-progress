def count_vowels(text):
    vowels = "aeiou"
    count = 0

    for char in text.lower():
        if char in vowels:
            count += 1

    return count


# print(count_vowels("hello"))
# print(count_vowels("education"))
# print(count_vowels("PYTHON"))


# Getting the most frequent character in a string
def character_frequency(text):
    result = {}

    for char in text:
        if char in result:
            result[char] += 1
            result
        else:
            result[char] = 1
    return result

print(character_frequency("banana"))

def most_frequent_char(text):
    count = character_frequency(text)
    frequent = 0
    for char in count:
        if count[char] > frequent:
            frequent = count[char]
            result = char

    return result

print(most_frequent_char("banana"))
