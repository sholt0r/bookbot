#!/usr/bin/env python

import sys

from stats import get_num_characters, get_num_words, sort_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main(book_path):
    # Get Values
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_characters(text)
    dict_list = sort_dict(num_chars)

    # Print Report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in dict_list:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")
    print("============= END ===============")

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main(sys.argv[1])
