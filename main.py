def main():
    # Print the book to the console
    text = get_the_book("books/frankenstein.txt")
    print(text)

def get_the_book(path):
    # Open and read the file from the path
    with open(path) as f:
        return f.read()



main()