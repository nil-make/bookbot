def get_num_words(get_book_text):
    return len(get_book_text.split())

def get_num_chars(get_book_text):
    num_chars = {}
    lowercase = get_book_text.lower()
    for character in lowercase:
        if character not in num_chars:
            num_chars[character] = 1
        else:
            num_chars[character] += 1
    return num_chars

def sort_on(item):
    return item["num"]

def sort_chars(num_chars):
    chars = []
    for character in num_chars:
        if character.isalpha() is True:
            char_dict = {}
            char_dict["char"] = character
            char_dict["num"] = num_chars[character] 
            chars.append(char_dict)
    chars.sort(reverse=True, key=sort_on)
    return chars

