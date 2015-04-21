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
        lettersLength = len(myLetterList)
        myWords = [''.join(result) for result in permutations(myLetters)]

        with open("/usr/share/dict/words", 'rb') as defaultWords:
            for word in myWords:
                if word in defaultWords:
                    myWords.append(word)

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