import random

# load word list
def load_words(WORDLIST_FILENAME):
    wordlist = list()
    # 'with' can automate finish 'open' and 'close' file
    with open(WORDLIST_FILENAME) as f:
        # fetch one line each time, include '\n'
        for line in f:
            # strip '\n', then append it to wordlist
            wordlist.append(line.rstrip('\n'))
    return wordlist

# select a word
def choose_word(wordlist):
    return random.choice(wordlist)

wordlist = load_words('wordlist.txt')
