def main():
    # Print the book to the console
    text = get_the_book("books/frankenstein.txt")
    #print(text)
    #print(f"This document contain {word_counter(text)} words")
    print(f"This is how many characters it contains {character_counter(text)}")
    

def get_the_book(path):
    # Open and read the file from the path
    with open(path) as f:
        return f.read()

def word_counter(text):
    # Count all words in the book
    words = text.split()
    return len(words)

def character_counter(text):
    counters_list = []
    char_counter = {}
    # Count all characters in the book
    uniq_char = set()
    low_text = text.lower()
    # Make a set of uniqe chars
    for char in low_text:
        uniq_char.add(char)

    uniq_char = list(uniq_char)
    #counter_list = [len(uniq_char)]
    for char in low_text:
        for i in range(len(uniq_char)):
            if char == uniq_char[i]:
                counter_list[i] += 1
                i += 1

    # Filling dictionary with data from 2 lists
    for i in range(len(uniq_char)):
        char_counter[uniq_char[i]] = counters_list[i]
        i += 1

    return char_counter    




main()