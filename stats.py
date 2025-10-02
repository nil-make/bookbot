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