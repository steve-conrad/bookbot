##Bookbot

book_path = "./books/frankenstein.txt"

def get_book_text(r):
        with open(r) as f:
            read_data = f.read()
        return read_data
def main():
    output = get_book_text(book_path)
    print(output)
main()
