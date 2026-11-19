def validate_password(password):
    if not password:
        return False
    has_digit = False
    has_uppercase = False

    if len(password) < 8:
        return False
    else:
        for char in password:
            if char.isdigit():
                has_digit = True
                
            if char.isupper():
                has_uppercase = True
           
        return has_digit and has_uppercase

# print(validate_password("Python123"))
# print(validate_password("python123"))
# print(validate_password("Pythonabc"))
# print(validate_password("Py1"))


def longest_word(sentence):
    words = sentence.split()

    longest = 0
    for word in words:
        if len(word) > longest:
            longest = len(word)
            new = word
        
    return new

# print(longest_word("Python makes coding fun"))
# print(longest_word("My name is Precious Oluwaseyi"))
