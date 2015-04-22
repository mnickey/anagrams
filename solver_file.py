__author__ = 'MNickey'

from collections import defaultdict
words = defaultdict(list)
with open("/usr/share/dict/words") as f:
    for word in f:
        word=word.strip()
        words[''.join(sorted(word))].append(word)

import sys
for word in sys.argv[1:]:
    myWords = (words[''.join(sorted(word))])

print "This is myWords", myWords