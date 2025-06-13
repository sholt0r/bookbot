def get_num_words(text):
    return len(text.split())

def get_num_characters(text):
    char_count = {}
    for char in text.lower():
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    return char_count

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    sorted_dicts = []
    for k, v in dict.items():
        sorted_dicts.append({"char": k, "num": v})

    sorted_dicts.sort(reverse=True, key=sort_on)

    return sorted_dicts
        
