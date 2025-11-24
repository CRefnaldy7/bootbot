def count_words(text):
    words = text.split()
    return len(words)

def sort_on(items):
    return items["num"]


def get_dictionary_characters(text):
    text = text.lower()

    result = {}
    for char in text:
        if result.get(char) is not None:
            result[char] += 1
        else:
            result[char] = 1
    return result

def get_list_of_dictionary(char_dict):
    result = []

    for char in char_dict:
        result_dict = {}
        result_dict["char"] = char
        result_dict["num"] = char_dict[char]
        result.append(result_dict)

    result.sort(reverse=True, key=sort_on)
    return result
