#Bookbot
import sys
from stats import get_word_count
from stats import count_chars
from stats import sort_on
from stats import sorted_characters

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(r):
        with open(r) as f:
            read_data = f.read()
        return read_data

def main():
    output = get_book_text(sys.argv[1])
    num_words = get_word_count(output)
    char_count = count_chars(output)
    sorted_chars = sorted_characters(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        char = item["char"]
        num = item["num"]
        # Only print if char is alphabetic
        if char.isalpha():
            print(f"{char}: {num}")

    print("============= END ==============")

main()
