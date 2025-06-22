#Bookbot
book_path = "./books/frankenstein.txt"
from stats import get_word_count
from stats import count_chars


def get_book_text(r):
        with open(r) as f:
            read_data = f.read()
        return read_data

def main():
    output = get_book_text(book_path)
    num_words = get_word_count(output)
    char_count = count_chars(output)
    print(num_words, "words found in the document")
    print(char_count)

main()
