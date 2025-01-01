def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    num_of_words = count_words(file_contents)
    num_of_chars = character_counter(file_contents)

    print(f"{num_of_words} words found in the document\n")
    
    list_of_dict = from_dict_to_list_of_dict(num_of_chars)
    list_of_dict.sort(reverse=True, key=sort_on)
    
    for dict in list_of_dict:
        print(f"The {dict["char"]} character was found {dict["num"]} times")
    


def count_words(text):
    counter = 0
    words = text.split()
    for word in words:
        counter += 1
    return counter
    #print(f"There is {counter} words in this book")

def character_counter(text):
    uniq_char = {}
    for char in text.lower():
        if char.isalpha():
            if char in uniq_char:
                uniq_char[char] += 1
            elif char not in uniq_char:
                counter = 1
                uniq_char[char] = counter       
    return uniq_char

def from_dict_to_list_of_dict(dict):
    list_of_dict = []
    for d in dict:
        new_dict = {}
        new_dict["char"] = d
        new_dict["num"] = dict[d]
        list_of_dict.append(new_dict)     
    return list_of_dict

def sort_on(dict):
    return dict["num"]



main()
