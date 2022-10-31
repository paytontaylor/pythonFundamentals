words = ['hello','goodbye','hi','bye']

# for word in words:
#     print(word)

def print_upper_words(words):
    """ Returns each word on a new line from a list of wordsp """
    for word in words:
        print(word.upper())

def print_upper_words2(words):
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())

def print_upper_words3(word, must_start_with):
    for letter in must_start_with:
         if word.startswith(letter):
                print(word.upper())
                break