from flask import Flask, render_template, request

app = Flask(__name__)

""" This is setting up the control dictionary to read against """
from collections import defaultdict
words = defaultdict(list)
with open("/usr/share/dict/words") as f:
    for word in f:
        word=word.strip()
        words[''.join(sorted(word))].append(word)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('main.html')
    else:
        #this is the original set of letters that I want anagrams for
        myLetters = request.form['letters']
        # some cleanup on those letters
        myLetters = ''.join(sorted(myLetters))
        # then assign those letters to 'word'
        word = myLetters.strip().lower()

        """ This is where I need to check the letter sets against the control group """
        myWords =  words[''.join(sorted(word))]
        return render_template('solver.html', myLetters = myLetters, myWords = myWords)

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port=5000)