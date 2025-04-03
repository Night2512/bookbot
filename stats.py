def get_book_word_count(book):
    words = book.split()
    count = len(words)
    return count

def get_book_character_count(book):
    words = book.split()
    letterList = {}
    for i in range (len(words)):
        word = list(words[i])
        for character in range (len(word)):
            if word[character].lower() in letterList:
                letterList[word[character].lower()] += 1
            else:
                letterList[word[character].lower()] = 1
    return letterList

def sort_high_to_low (num_characters):
    sorted_dict = dict(sorted(num_characters.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict