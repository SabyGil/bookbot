import sys
from stats import get_num_words
from stats import freqCounter
from stats import countDict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

bookText = None

if len(sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
else:
    bookText = get_book_text(sys.argv[1])

def printSummary(bookText):
    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    print(f'Found {len(bookText.split())} total words')
    print('--------- Character Count -------')
    sortedDict = countDict(freqCounter(bookText))
    for d in sortedDict:
        if not d['char'].isalpha():
            continue
        print(f'{d["char"]}: {d["num"]}')
    print("============= END ===============")
printSummary(bookText)
