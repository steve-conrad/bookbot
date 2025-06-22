def get_word_count(output):
    count = 0
    split = output.split()
    for word in split:
        count += 1
    return count

def count_chars(output):
    char_dict = {}
    lwr_case = str.lower(output)
    for char in lwr_case:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1 
    return char_dict

def sort_on(char_dict):
    return char_dict["num"]

def sorted_characters(char_counts):
    characters = []
    for char, num in char_counts.items():
        characters.append({"char": char, "num": num})

    characters.sort(reverse=True, key=sort_on)
    return characters
