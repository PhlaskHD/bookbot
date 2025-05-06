from stats import count_words, count_letters

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = count_words(text)
    print(f"{num_words} words found in the document")
    num_letters = count_letters(text)
    print(num_letters)

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents

main()