from stats import count_words
from stats import get_dictionary_characters
from stats import get_list_of_dictionary
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
        return contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    # print(get_dictionary_characters(book_text))
    # print(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")
    print("--------- Character Count -------")

    dict_characters = get_dictionary_characters(book_text)
    list_of_dict = get_list_of_dictionary(dict_characters)
    for char_report in list_of_dict:
        if (char_report["char"].isalpha()):
            print(f"{char_report['char']}: {char_report['num']}")

    print("============= END ===============")

main()