def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

from stats import get_num_words
from stats import get_num_chars
from stats import sort_on
from stats import sort_chars

def main():
    filepath = "./books/frankenstein.txt"
    num_words = get_num_words(get_book_text(filepath))
    print(f"Found {num_words} total words")
    num_chars = get_num_chars(get_book_text(filepath))
    get_num_chars(get_book_text(filepath))
    chars = sort_chars(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c in range (0, len(chars)):
        print(f"{chars[c]["char"]}: {chars[c]["num"]}")
    print("============= END ===============")

main()