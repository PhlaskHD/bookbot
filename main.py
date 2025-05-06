import sys
from stats import count_words, count_letters, dict_to_list

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    text = get_book_text(path)
    num_words = count_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    num_letters = count_letters(text)
    sorted_list = dict_to_list(num_letters)
    print("--------- Character Count -------")
    for each in sorted_list:
        print(f"{each["char"]}: {each["num"]}")
    print("============= END ===============")
    


def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents

main()