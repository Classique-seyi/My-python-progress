# def group_by_length(words):
#     word_dict = {}
    

#     for word in words:
#         word_list = []
#         key = len(word)
#         if key in word_dict:
#             word_list.append(word)
#             word_dict[key] += word_list
#         else:
#             word_list.append(word)
#             word_dict[key] = word_list
            
        
#     return word_dict

def group_by_length(words):
    word_dict = {}
    

    for word in words:
        key = len(word)
        if key in word_dict:
            word_dict[key].append(word)
        else:
            word_dict[key] = [word]

    return word_dict

print(group_by_length(["cat", "dog", "apple", "hi", "book"]))


# Finding the top_scoring student
def top_student(scores):
    top_name = scores
    top_score = scores[key]
    for key, value in scores.items():
        
        if value > top_score:
            top_score = value
    return top_score

scores = {
    "Ada": 78,
    "Tunde": 92,
    "Mira": 85,
    "John": 92
}

print(top_student(scores))


