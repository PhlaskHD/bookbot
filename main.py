def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = count_words(text)
    print(f"{num_words} words found in the document")

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents

def count_words(text):
    word_list = text.split()
    return len(word_list)

main()