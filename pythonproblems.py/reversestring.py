# Reversing a string
def reverse_string(text):
    if not text:
        return None
    new_text = ""
    for char in text:
        new_text = char + new_text
    return new_text


print(reverse_string("python"))


# Calculating the average of the length of words in a list
def get_lengths(words):
    new_list = []
    for word in words:
        length = len(word)
        new_list.append(length)
    return new_list

def average_length(words):
    new_list = get_lengths(words)
    total = 0
    average = 0

    for word in new_list:
        total += word

    average = total / len(new_list)

    return average

print(get_lengths(["cat", "tiger", "ox"]))
print(average_length(["cat", "tiger", "ox"]))


