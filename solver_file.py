__author__ = 'Michael Nickey'
# Modified by: 'Michael Nickey'

import sys
from collections import defaultdict
words = defaultdict(list)
myWords = []

def find_anagrams(letters):
    with open("/usr/share/dict/words") as f:
        for word in f:
            word=word.strip()
            words[''.join(sorted(word))].append(word)
    for word in sys.argv[1:]:
        myWords.append( [''.join(sorted(word))] )
    return myWords


# Original Work
# from collections import defaultdict
# words = defaultdict(list)
# with open("/usr/share/dict/words") as f:
#     for word in f:
#         word=word.strip()
#         words[''.join(sorted(word))].append(word)
#
# import sys
# for word in sys.argv[1:]:
#     print(words[''.join(sorted(word))])
