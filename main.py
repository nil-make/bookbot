def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

from stats import get_num_words
from stats import get_num_chars

def main():
    num_words = get_num_words(get_book_text("./books/frankenstein.txt"))
    print(f"Found {num_words} total words")
    num_chars = get_num_chars(get_book_text("./books/frankenstein.txt"))
    print(num_chars)
main()