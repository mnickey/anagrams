from flask import Flask, render_template, request
from itertools import permutations

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('main.html')
    else:
        myLetters = request.form['letters']
        myLetters = ''.join(sorted(myLetters))
        myLetters = myLetters.strip()

        myWords = []
        myLetterList = list(myLetters)
        # lettersLength = len(myLetterList)
        # myWords = [''.join(result) for result in permutations(myLetters)]
        # myWords = sorted(myWords)

        # with open("/usr/share/dict/words") as defaultWords:
        #     words = set(line.strip() for line in defaultWords)
        #     for word in words:
        #         if word not in words:
        #             myWords.remove(word)
        #             defaultWords.seek(0) #move the seek position back to original area.


        #From rousav at Thinkful
        from collections import defaultdict
        words = defaultdict(list)
        with open("/usr/share/dict/words") as f:
            for word in f:
                word=word.strip()
                words[''.join(sorted(word))].append(word)

        import sys
        for word in words:
            myWords = (words[''.join(sorted(word))])

            # for x in myLetterList:
            #     for word in defaultWords:
            #         if x in word and len(word) == (lettersLength + 1):
            #             if word in myWords: #Check for existing word
            #                 continue
            #             else:
            #                 myWords.append(word)
        return render_template('solver.html', myLetters = myLetters, myWords = myWords)

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port=5000)