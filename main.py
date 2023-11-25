
FILE_PATH = "books/frankenstein.txt"

def main():
    file_contents = read_file(FILE_PATH)
    num_letters = count_letters(file_contents)
    num_letters_sorted = sorted(num_letters.items(), key=lambda x: x[1], reverse=True)
    num_words = count_words(file_contents)
    print_report(num_letters_sorted, num_words)


def read_file(file_path):
    with open(file_path, "r") as file:
        file_contents = file.read()
        return file_contents

def count_words(file_contents):
    return len(file_contents.split())
    
def count_letters(file_contents):
    num_letters = {}
    for letter in file_contents:
        lower_letter = letter.lower()
        if lower_letter.isalpha():
            if lower_letter in num_letters:
                num_letters[lower_letter] += 1
            else:
                num_letters[lower_letter] = 1
    return sort_letters(num_letters)

def sort_letters(num_letters):
    return dict(sorted(num_letters.items(), key=lambda x: x[1], reverse=True))


def print_report(num_letters, num_words):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print("")
    for letter in num_letters:
        print(f"The '{letter[0]}' character was found {letter[1]} times")
    print("--- End report ---")

main()