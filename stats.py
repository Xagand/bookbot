def count_words(text):
    counter = 0
    words = text.split()
    for word in words:
        counter += 1
    return counter