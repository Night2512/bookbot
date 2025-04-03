import sys
from stats import *

if len(sys.argv) < 2:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

def get_book_text(book): 
    with open(book) as f:
        file_contents = f.read()
        return file_contents
    
def main () :
    read = get_book_text(path)
    num_words = get_book_word_count(read)
    print ("============ BOOKBOT ============")
    print ("Analyzing book found at books/frankenstein.txt...")
    print ("----------- Word Count ----------")
    print (f"Found {num_words} total words")
    print ("--------- Character Count -------")
    num_characters = get_book_character_count(read)
    sorted_characters = sort_high_to_low(num_characters)
    for character in sorted_characters:
        count = sorted_characters[character]
        print (f"{character}: {count}")
    print ("============= END ===============")

main()