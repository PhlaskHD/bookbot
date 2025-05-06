def count_words(text):
    word_list = text.split()
    return len(word_list)

def count_letters(text):
    lower_text = text.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    count_dict = {}
    for char in alphabet:
        count_dict[char] = 0
    for char in lower_text:
        if char in count_dict:
            count_dict[char] += 1
    return count_dict