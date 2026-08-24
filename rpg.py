def create_character(character_name, strength, intelligence, charisma):
    if not isinstance(character_name, str):
        return "The character name should be a string"
    elif character_name == "":
        return "The character should have a name"
    elif len(character_name) > 10:
        return "The character name is too long"
    for char in character_name:
        if char == " ":
            return "The character name should not contain spaces"
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return "All stats should be integers"
    elif strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    elif strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
    total_stats = strength + intelligence + charisma
    if not total_stats == 7:
        return "The character should start with 7 points"
    full_dot = '●'
    empty_dot = '○'
    strengths = full_dot * strength
    strengthsdot = (10 - strength) * empty_dot
    intelligences = full_dot * intelligence
    intelligencesdot = (10 - intelligence) * empty_dot
    charismas = full_dot * charisma
    charismasdot = (10 - charisma) * empty_dot
    return f'{character_name}\nSTR {strengths}{strengthsdot}\nINT {intelligences}{intelligencesdot}\nCHA {charismas}{charismasdot}'
    

create_character('ren', 4, 2, 1)
print(create_character('Tosin', 3, 2, 2))

