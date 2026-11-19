def first_non_repeating(text):

    if not text:
        return None
    else:
        for char in text:
            count = text.count(char)
            if count == 1:
                return char

    

print(first_non_repeating("swiss"))