##Bookbot

book_path = "./books/frankenstein.txt"

def get_book_text(r):
        with open(r) as f:
            read_data = f.read()
        return read_data

def get_word_count():
    contents = get_book_text(book_path)
    count = 0
    split = contents.split()
    for word in split:
        count += 1
    return count

def main():
    output = get_book_text(book_path)
    num_words = get_word_count()
    print(num_words, "words found in the document")

main()
